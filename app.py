# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

# load data

columns = ["checking_ac", "duration", "credit_history", "purpose", "amount", "saving_ac",
        "employment_status", "installment_rate", 'personal_status_sex', "debtor_guarantor", "residence_since",
        "property", "age", "installment_plan", "housing", "existing_credits", "job", "liable_count", "telephone",
        "foreign_worker", "target"]
df = pd.read_csv("./data/german.data2.csv", delimiter=' ', index_col=False, names=columns)
# print(set(list(df.housing)))

cat_dict = {
    "A11": "-0",
    "A12": "0-200",
    "A13": "200+",
    "A14": "no checking acc",
    "A30": "no credit",
    "A31": "all paid duly",
    "A32": "existing paid duly",
    "A33": "payment delay",
    "A34": "critical acc",
    "A40": "car (new)",
    "A41": "car (old)",
    "A42": "furniture/equipment",
    "A43": "radio/television",
    "A44": "domestic appliances",
    "A45": "repairs",
    "A46": "education",
    "A47": "vacation",
    "A48": "retraining",
    "A49": "business",
    "A410": "others",
    "A61": "-100",
    "A62": "100-500",
    "A63": "500-1000",
    "A64": "1000+",
    "A65": "no acc",
    "A71": "unemployed",
    "A72": "-1",
    "A73": "1-4",
    "A74": "4-7",
    "A75": "7+",
    "A91": "male-div/sep",
    "A92": "male-single",
    "A93": "male-married",
    "A94": "female-div/sep/mar",
    "A95": "female-single",
    "A101": "none",
    "A102": "co-applicant",
    "A103": "guarantor",
    "A121": "real est",
    "A122": "building",
    "A123": "car",
    "A124": "none",
    "A141": "bank",
    "A142": "store",
    "A143": "none",
    "A151": "rent",
    "A152": "own",
    "A153": "free",
    "A171": "unempl-no res",
    "A172": "unempl-res",
    "A173": "empl",
    "A174": "high empl",
    "A191": "yes",
    "A191": "no",
    "A201": "yes",
    "A202": "no"}

df.replace(cat_dict, inplace=True)
df.target.replace({2: 0}, inplace=True)

app = dash.Dash()



app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': list(set(list(df.housing))), 'y': list(df.housing.value_counts()), 'type': 'bar'}
            ],
            'layout': {
                'title': 'Housing Count'
            }
        }
    )
])

def get_data():

    return df

if __name__ == '__main__':
    app.run_server(debug=True)