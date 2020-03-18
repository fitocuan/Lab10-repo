for i in ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca', 'thal']:
    print("{0} = request.form['{0}']".format(i))
