# Antimalarial activity for sexual stage and asexual blood stage (ABS)

Prediction of the antimalarial potential of small molecules using data from various chemical libraries that were screened against the asexual and sexual (gametocyte) stages of the parasite. Several compounds molecular fingerprints were used to train machine learning models to recognize stage-specific active and inactive compounds.

This model was incorporated on 2023-07-10.Last packaged on 2025-10-17.

## Information
### Identifiers
- **Ersilia Identifier:** `eos80ch`
- **Slug:** `malaria-mam`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Malaria`, `P.falciparum`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of inhibition of the malaria parasite growth

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| sexual_stage | float | high | Probability score of inhibition of the sexual stage (gametocytes) of the malaria parasite |
| asexual_blood_stage | float | high | Probability score of inhibition of the asexual blood stage (ABS) of the malaria parasite |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos80ch](https://hub.docker.com/r/ersiliaos/eos80ch)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos80ch.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos80ch.zip)

### Resource Consumption
- **Model Size (Mb):** `12`
- **Environment Size (Mb):** `631`
- **Image Size (Mb):** `676.36`

**Computational Performance (seconds):**
- 10 inputs: `28.01`
- 100 inputs: `18.11`
- 10000 inputs: `68.94`

### References
- **Source Code**: [https://github.com/M2PL](https://github.com/M2PL)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acsomega.3c05664](https://pubs.acs.org/doi/10.1021/acsomega.3c05664)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos80ch
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos80ch
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
