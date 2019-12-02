# karaoke

Randomizing google sheets for karaoke purposes

## Usage

1. You'll need a service account with the "Slides API" enabled.
You can start that [here](https://console.cloud.google.com/iam-admin/serviceaccounts/create).
Then share the slide deck with your service account email.
2. Download the JSON credientials file for the service account to your computer `/path/to/cred/file.json`.
3. Create a file in this directory called `config.json` with the contents:
```json
{
  "cred_file": "/path/to/cred/file.json",
  "deck_id": "the random id for your slide deck"
}
```
4. Create a conda environment:
```bash
conda env create --prefix ./env -f environment.yml
conda activate ./env
```
5. Run the script:
```bash
python randomize.py
```
