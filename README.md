# Whatsapp-api

Well I should not name it as api but I name it.
So before beliebing this program wildly, test well before use.

## Usage

Open whatsapp web on brower and click on the contact you want to send messages to. Open this program in vs code. Keep both vs-code as well as chrome maximised. Then if your screen resolution is 1980*1080 then this programm will flood the message to recipient.

```bash
conda activate ./env
python ./automate.py
```

## Building the Conda environment

After adding any necessary dependencies that should be downloaded via `conda` to the 
`environment.yml` file and any dependencies that should be downloaded via `pip` to the 
`requirements.txt` file you create the Conda environment in a sub-directory `./env`of 
your project directory by running the following commands.

```bash
mamba env create --prefix ./env --file environment.yml --force
```

Once the new environment has been created you can activate the environment with the following 
command.

```bash
conda activate $ENV_PREFIX
```