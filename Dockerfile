FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2022.9.2
RUN pip install scikit-learn==1.2.2
RUN pip install joblib==1.2.0

WORKDIR /repo
COPY . /repo
