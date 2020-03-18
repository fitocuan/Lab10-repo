for i in ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca', 'thal']:
    print('<label for="{0}"></label>'.format(i))
    print('<input type="number" id="{0}" name="{0}"'.format(i))
