#!/usr/bin/env python
# coding: utf-8

# Import Dependencies
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers


def run_model(chosenstats):

    # read in the model csv
    model_df = pd.read_csv("modelPython.csv")

    predict2020 = pd.read_csv('draft2020.csv')
    # create a df of the subjects matched by ID
    subjects = model_df[['ID', 'Player_x', 'FirstNm', 'LastNm']]
    subjects2020 = predict2020[['ID', 'Player_x', 'FirstNm', 'LastNm']]

    # Convert Age, weight, and height columns to floats
    model_df[['Wt', 'height']] = model_df[['Wt', 'height']].astype(float)

    model_df.drop(columns=['Player_x', 'FirstNm', 'LastNm'], inplace=True)

    # Add year and ID to chosenstats
    chosenstats.append('year')
    chosenstats.append('ID')
    chosenstats.append('FPTS')

    # handle option to run model without players that didn't score any FPTS in the NFL
    if 'ExcludeZeroFPTS' in chosenstats:
        exclude = True
        chosenstats.remove('ExcludeZeroFPTS')
    else:
        exclude = False

    model_df = model_df[chosenstats]

    # drop 1 columns associated with each set of dummy variables created
    if 'Class' in chosenstats:

        if 'Conf' in chosenstats:
            print("found Conf and Class")
            # Create dummy variables for
            model_df = pd.get_dummies(model_df)
            model_df = model_df.drop(columns=['Class_SR'])
            model_df = model_df.drop(columns=['Conf_WAC'])
        else:
            print("found Class")
            # Create dummy variables for
            model_df = pd.get_dummies(model_df)
            model_df = model_df.drop(columns=['Class_SR'])
    else:
        if 'Conf' in chosenstats:
            print("found Conf")
            model_df = pd.get_dummies(model_df)
            model_df = model_df.drop(columns=['Conf_WAC'])
        else:
            print("neither class or conference selected")

    # Create df of players that I want to predict who were drafted in 2020
    pre2020draft = model_df[model_df['year'] == 2020]

    # drop irrelevant columns of ID and year that I kept til now to verify I would know the subjects and be able to separate
    # out for year after creating dummy variable.  Technically if I wanted to keep year I should make it categorical
    model_df.drop(columns=['year', 'ID'], inplace=True)
    pre2020draft.drop(columns=['year', 'ID', 'FPTS'], inplace=True)

    # Limiting training data if someone choose to not use players with 0 fantasy points
    if exclude:
        model_df = model_df[model_df['FPTS'] > 0]
    else:
        pass

    # define x the inputs and y the actuals
    X = model_df.drop(columns=['FPTS'])
    y = model_df['FPTS'].values.reshape(-1, 1)
    print(X.shape, y.shape, pre2020draft.shape)

    #store length of inputs to pass into model
    size = len(X.columns)
    print(size)
    # Split the data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.9, random_state=28)

    # define the model

    def build_model():
        model = keras.Sequential([
            layers.Dense(3*size, activation='relu', input_dim=size),
            # layers.Dense(2*size, activation='relu'),
            #     layers.Dense(90, activation='relu'),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    # build model for all data
    model = build_model()


    # fit training data to the model
    model.fit(
        X_train,
        y_train,
        epochs=60,
        shuffle=True,
        verbose=0
    )

    #run 2020 players through the model
    projected = model.predict(pre2020draft)

    #add projected points to the subjects
    subjects2020['projected points'] = projected

    #Sort by projected points
    subjects2020.sort_values('projected points', ascending=False, inplace=True)

    #drop unecessary columns
    subjects2020.drop(columns=['FirstNm', 'LastNm', 'ID'], inplace=True)

    #reset the index
    subjects2020.reset_index(inplace=True)

    # Add rank column 
    subjects2020['Rank'] = subjects2020['index']+1

    # reformat data for web display
    web_display = subjects2020[['Rank', 'Player_x', 'projected points']]

    web_display
    # #get data in a format to write to a file that can be read by webpage
    data = web_display.to_dict('records')

    # get data in a format to write to a file that can be read by webpage
    data = web_display.to_dict('dict')


    return data
