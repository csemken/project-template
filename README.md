# Project template

## Usage

This is a reusable project template.
To use it:

1. Create a fork of the repository
2. Adjust this README and the wiki
3. Update the dvc remote in `.dvc/config` and push existing files
4. Remove test data and module
5. (Optional) Enable the automatic synchronization with a LaTeX/overleaf mirror repo:
    1. Create a mirror repo on GitHub (e.g., project-template-latex), ticking the box “Add a README file” to create an initial commit
    3. Generate and save an access token for the mirror repo: (Account) Settings → Developer Settings → Personal access token → Generate new token
        - Expiration → select date far in future
        - Only selected repositories → Select the new mirror repo
        - Permissions → Contents: Read and write
    4. Set two secrets in the main (i.e., this) repo: (Repository) Settings → Secrets and variables → Actions → New repository secret
        1. LATEX_REPOSITORY: `your_mirror_repo` (e.g., csemken/project-template-latex)
        2. LATEX_TOKEN: `your_token` (e.g, github_pat_...)
    5. Make a change and push it to the main repo
    6. Import the project on overleaf: New project → Import from GitHub → `your_mirror_repo` → Import to Overleaf
    7. Set the main document: Menu → Main document → paper.tex

## File structure

```
analysis       # code for data analysis
└── *          # module
bin            # maintenance scripts
config         # configuration files
data           # data
├── raw        # raw input data
│   └── *      # source
├── input      # input data
│   └── *      # module
├── output     # output data
│   └── *      # module
└── release    # publication output
paper_slides   # tex code
├── release    # -> /data/release/
└── *          # manually created assets
```

## Getting started

The [manual](wiki/Introduction) in the wiki explains the general setup.
The analysis setup is explained in `analysis/README.md`.
