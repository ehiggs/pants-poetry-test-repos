poetry_requirements()

python_sources(name="lib")

pex_binary(
    name="project-app-async-exec",
    entry_point="app",
    execution_mode='venv',
    dependencies=[
        ':project-app-async',
	':lib',
	'project-models:lib',
    ],
)
