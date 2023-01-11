poetry_requirements()

python_sources(
	name="lib", 
	dependencies=[
	":project-models", 
	"project_models:lib"
	]
)

python_distribution(
	name="dist",
	dependencies=[":lib", ":project-models"],
	wheel=True,
	sdist=True,
	provides=setup_py(
		name="project_models",
		version="0.0.1",
		description="Project model.",
	),
)
