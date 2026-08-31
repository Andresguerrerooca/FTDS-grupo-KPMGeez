# Git: guía práctica para el equipo

Tutorial autocontenido para quienes no han usado Git en un trabajo de asignatura. El objetivo es **no perder trabajo**, **dejar rastro de quién hizo qué** y **no subir secretos ni datos**.

Esta guía **no** recomienda `git push --force`, `git reset --hard` ni otros comandos destructivos como parte del flujo normal.

## 1. Palabras que hay que entender

| Término | Significado sencillo |
| --- | --- |
| **Repositorio** | La carpeta del proyecto más el historial de cambios que guarda Git. |
| **Área de trabajo** | Los archivos tal como están ahora en tu disco (`working tree`). |
| **Staging** (índice) | La «bandeja» de lo que entrará en el *próximo* commit (`git add`). |
| **Commit** | Una instantánea con mensaje, autora/autor y fecha. No se «envía» solo con commit: eso es local hasta el `push`. |
| **Rama** | Una línea de trabajo. `main` (o `master`) suele ser la estable del equipo; vuestras tareas van en ramas cortas. |
| **Remoto** | La copia en GitHub, GitLab, Bitbucket, etc. Suele llamarse `origin`. |
| **Pull request / merge request** | Petición de incorporar una rama a otra, con revisión. En GitHub: *Pull Request*. En GitLab: *Merge Request*. El equipo puede usarlo o fusionar en local si el profesorado no exige PR. |

## 2. Configuración inicial (una vez por ordenador)

Sustituid por vuestro nombre y el correo **académico** (o el que acordéis). Git los escribe en cada commit.

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "nombre.apellido@correo.universidad.es"
```

Comprobación:

```bash
git config --global --list
```

No hace falta publicar el correo en el README. Sí debe ser identificable para el profesorado.

## 3. Clonar o inicializar

**Clonar** (lo habitual si ya existe el repo del equipo):

```bash
git clone https://ejemplo.invalid/equipo/ftds-albamarket.git
cd ftds-albamarket
```

**Inicializar** (si partís de la carpeta plantilla sin Git):

```bash
cd ruta/del/proyecto
git init
git add README.md
git status
```

Añadid el remoto cuando exista:

```bash
git remote add origin https://ejemplo.invalid/equipo/ftds-albamarket.git
```

(URL de ejemplo; usad la vuestra.)

## 4. Comandos de uso diario (no destructivos)

### Ver el estado

```bash
git status
```

Os dice la rama, archivos modificados y qué está en staging.

### Ver diferencias

```bash
git diff
git diff --staged
```

El primero: trabajo vs staging. El segundo: staging vs último commit.

### Añadir al staging y confirmar

```bash
git add sql/05_transform_load.sql
git add docs/plantillas/registro_insights.md
git commit -m "sql: carga inicial de pedidos a core con regla de nulos"
```

`git add .` añade todo lo no ignorado. Usadlo con cuidado: mirad `git status` antes.

### Historial

```bash
git log
git log --oneline --decorate --graph -n 20
```

### Integrar trabajo del remoto

```bash
git pull
```

Trae commits nuevos y, por defecto, fusiona. Hacedlo **al empezar la sesión**.

### Publicar vuestra rama

```bash
git push
git push -u origin nombre-de-la-rama
```

La primera vez de una rama nueva hace falta `-u origin ...`. **No** uses `--force`.

### Ramas

```bash
git branch
git branch feature/staging-customers
git switch feature/staging-customers
```

`git switch` cambia de rama (equivalente moderno de `git checkout` para este uso).

Volver a la principal:

```bash
git switch main
```

(Si vuestra principal se llama `master`, usad ese nombre.)

### Fusionar

En la rama de destino (normalmente `main`), con el trabajo ya revisado:

```bash
git switch main
git pull
git merge feature/staging-customers
```

Si hay conflicto, Git lo marca: no borréis el archivo de otra persona. Ved la sección 6.

### Descartar cambios **no confirmados** de un archivo (recuperable si el editor tiene copia)

```bash
git restore sql/05_transform_load.sql
```

Esto vuelve el archivo al último commit (o al staging, según opciones). Solo para cambios que **sí queréis tirar**. No lo uses sobre trabajo ajeno.

Quitar del staging sin perder el archivo:

```bash
git restore --staged sql/05_transform_load.sql
```

## 5. Flujo recomendado por equipo

1. Una **rama corta por tarea** (`feature/vistas-mensuales`, `fix/fk-orders`).
2. **Commits pequeños** que se puedan explicar en una frase.
3. `git pull` al empezar (en vuestra rama, o actualizad `main` y fusionad).
4. **Revisión** (PR/MR o revisión en pareja) antes de integrar en `main`.
5. No trabajéis durante días solo en local sin `push`: si el disco falla, el equipo no tiene vuestra parte.

Evita una rama eterna `trabajo-de-ana` donde se mezcla SQL, el informe y el dashboard.

## 6. Conflicto sencillo (sin borrar trabajo ajeno)

Tras `git merge` o `git pull`, un archivo puede contener marcas:

```text
<<<<<<< HEAD
vuestra versión
=======
la otra versión
>>>>>>> feature/otra
```

Pasos:

1. Abrid el archivo y **entendéis ambas partes**.
2. Dejad el resultado combinado (a menudo las dos aportaciones).
3. Eliminad las marcas `<<<<<<<`, `=======`, `>>>>>>>`.
4. `git add` ese archivo y `git commit` para cerrar el merge (si Git lo pide).

Si no estáis seguros, pedid a quien escribió el otro bloque. **No** borréis su función para que «compile lo mío».

## 7. Antes de cada sesión y antes de entregar

**Al empezar**

- `git status` (¿estoy en la rama correcta?)
- `git pull`
- Activar `.venv`

**Antes de entregar**

- `git status` limpio (o solo archivos que no deban subirse, ignorados)
- `git log` coherente
- Etiqueta recomendada: `entrega-1` o `entrega-2` (el profesorado puede pedir otra)
- Comprobar que no hay CSV, `.env`, `.sqlite`, `.venv`
- Push de `main` (o la rama que se evalúe) **como máximo el día posterior a la presentación**, según las rúbricas

```bash
git tag entrega-1
git push origin entrega-1
```

(Solo cuando el equipo esté de acuerdo y el remoto lo permita.)

## 8. Mensajes de commit

Adecuados:

- `sql: crea tablas staging de pedidos y líneas`
- `docs: añade cautelas de calidad al insight 03`
- `fix: corrige tipo DATE en core.orders.order_date`

Inadecuados:

- `cambios`
- `asdf`
- `final finalisimo`
- `wip` reiterado sin contexto
- `update` (¿de qué?)

El mensaje responde a *por qué / qué aporta este commit*, no a *he tocado archivos*.

## 9. `.gitignore`

El archivo `.gitignore` de la raíz indica qué **no** debe entrar al repo. Git dejará de proponer esos archivos (si nunca se añadieron).

Prohibido subir, aunque `git add .` sea tentador:

- `.env` y cualquier contraseña
- `.streamlit/secrets.toml` (el `.example` sí puede subirse)
- bases `.db`, `.sqlite`, `.sqlite3`
- ficheros de `data/raw/` y `data/processed/`
- `.venv/` y otros entornos
- `__pycache__/`, `.pytest_cache/`
- logs, temporales, exportaciones grandes, volcados de base

Si un archivo prohibido **ya** está en el historial, no basta con borrarlo del disco: seguirá en Git. Avisad al profesorado; no intentes reescribir historia con `--force` por vuestra cuenta.

## 10. Recuperación ante errores comunes (checklist)

| Situación | Qué hacer | Qué no hacer |
| --- | --- | --- |
| Modifiqué un archivo y quiero deshacer **antes** de `add`/`commit` | `git restore archivo` si estáis seguros | `git reset --hard` |
| Hice `add` demasiado amplio | `git restore --staged archivo` | Seguir con commit a ciegas |
| Commit local último con mensaje mal (aún no hay push) | En esta asignatura, haced un commit nuevo que corrija; evitad reescribir | `commit --amend` si no domináis el flujo |
| Conflicto de merge | Editar a mano, conservar ambas lógicas | Borrar el archivo «para que desaparezca el conflicto» |
| Push rechazado | `git pull` (o `git pull --rebase` solo si el equipo lo domina), resolver, `git push` | `git push --force` |
| Subí un CSV o `.env` | Decídlo en clase; rotad la contraseña si era real | Dejarlo y «ya lo quitamos luego» |
| Estoy en la rama equivocada | `git status`, `git switch` a la correcta **si no hay commits** o commitad antes en la rama actual | Copiar archivos a ciegas con el Explorador sobre `.git` |

**No uses** en el flujo normal:

- `git push --force` (ni `--force-with-lease` si no os lo han enseñado)
- `git reset --hard`
- borrar la carpeta `.git` para «empezar de cero» con trabajo de otras personas dentro

## 11. Chuleta

```bash
git status
git diff
git add <archivo>
git commit -m "tipo: resumen"
git log --oneline -n 10
git pull
git push
git branch
git switch <rama>
git switch -c <rama-nueva>
git merge <rama>
git restore <archivo>
git restore --staged <archivo>
git tag entrega-1
```

Más contexto del curso: [README](../README.md), [flujo](03_flujo_de_trabajo_del_proyecto.md), [FAQ](08_preguntas_frecuentes.md).
