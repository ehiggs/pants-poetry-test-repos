poetry_requirements()

python_sources(name="lib")

pex_binary(
    name="project-app-exec",
    entry_point="app",
    execution_mode='venv',
    dependencies=[
        ':project-app',
	':lib',
	'project-models:lib',
    ],
)
