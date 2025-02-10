from flask import Flask, render_template
import plotly.express as px
from models import User, WorkoutLog, PerformanceStats, engine
from sqlmodel import Session, select

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    with Session(engine) as session:
        statement = select(WorkoutLog)
        logs = session.exec(statement).all()
    
    # Convert logs to a DataFrame
    df = pd.DataFrame([log.dict() for log in logs])
    fig = px.bar(df, x="workout_date", y="weight", color="workout_name_id", title="Workout Performance")
    graph = fig.to_html(full_html=False)
    
    return render_template('dashboard.html', graph=graph)

if __name__ == "__main__":
    app.run(debug=True)