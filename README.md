# Antimalarial activity (ABS and sexual stages)

Prediction of the antimalarial potential of small molecules using data from various chemical libraries that were
screened against the asexual and sexual (gametocyte) stages of the parasite. Several
compounds’ molecular fingerprints were used to train machine learning models to recognize stage-specific
active and inactive compounds.

## Identifiers

* EOS model ID: `eos80ch`
* Slug: `malaria-mam`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Probability of inhibition of the malaria parasite growth

## References

* [Publication](https://pubs.acs.org/doi/10.1021/acsomega.3c05664)
* [Source Code](https://github.com/M2PL)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos80ch)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos80ch.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos80ch) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/acsomega.3c05664) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!