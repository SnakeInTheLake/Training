# RnD-42 project  
Kaggle InClass [competition](https://www.kaggle.com/c/rnd-42-welcome).
We solve a binary classification problem over a dataset without a description of its columns. The only known things about data are:
- Each row in both train and test datasets has a unique ID.
- Each row in the dataset represents an event that occurred at the time represented by "DT" column and we try to predict: if the same event occurs at least one more time until the end of the day. "1" in the target means that it will occur, "0" - no.
- Columns with the "N_" prefix represent numeric features, with the "C_" prefix - сategorial features. All these features describe somehow the person, who raised the event or the previous history of such events raised by this person or environmental conditions at the time of the event. 

**Gathered skills:** Data preprocessing, Working with anonymized data, Model selection, Hyperparameters tuning with `hyperopt`.
