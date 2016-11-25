# SNPS Yuefan

----

## Active AIs

- Update Tuan enter/leave logic in `views.py`; Add related buttons in template. (Leo)
- Update template to reuse html blocks for repeated content. (Leo)
- Migrate to bootstrap3. (Jessie)
- Aggregate existing 3rd party js and css. (Jessie)
- Aggregate self-added CSS into a central CSS file. (Jessie, Lawrence)
- Model update and related view update. (Lawrence)
- Update Jumbotron to use Carousel. (Yimin)
- Continue user test. (Zoe)
- Collect pictures/logos/themes. (Zoe)
- Shift to use **Chinese** in webpage. (Lawrence, Jessie)
- Deploy Celery. (Yimin)

----

## Completed AIs

- Details 显示joined person list -- Yimin (Done)
- MyTuan显示 joined tuan list -- Yimin (Done)
- Details 专门开一个column -- Lawrence (Skipped)
- Navigator 做成模板 -- Lawrence (Done)
- MyTuan table 显示bug -- Zoe (Done)
- Authenticate decorator -- Leo (Done)
- Change to datatime to all table -- Jessie (Done)
- Use form view in my Tuan view -- Lawrence (Done)
- Login redirect might have bug. Cannot reproduce during meeting. -- Yimin (Done)
- db switch/population -- Lawrence (Done. population will be skipped for now.)

----

## Coding Conventions
- Use spaces instead of tabs for indentation, in all types of committed files.
- 4-space-indent for Python scripts.
- Use Unix-style line endings.
- Eliminate trailing blank characters.
- Remove unformatted debugging messages in committed files.

----

## Database Setup
###### Lawrence @ 2016/09/09
Following three files will be excluded from Git repository.
- `tuanproj/settings_local.py`
- `db.sqlite3`
- `django.db`

The default database is setup in `tuanproj/settings.py` and points to Leo's MySQL at `pvicc015:python_django`. To use this database, make sure `tuanproj/settings_local.py` doesn't exist, or this local setup file doesn't overwrite default database setup. Alternatively, to use custom database for local test, please place related setup in `tuanproj/settings_local.py`.

An example `settings_local.py` is at `tuanproj/settings_local.example.py`.
