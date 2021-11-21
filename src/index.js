import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import data from './data.json';

class Main extends React.Component {
  render () {
    let rankings = [<tr><th>Rank</th><th>Team</th><th>Rating</th></tr>];
    let rank_num = 1;
    for (let i in data['ranks']) {
      let team = data['ranks'][i][0];
      let team_key={"DAL":"Dallas Cowboys","PHI":"Philadelphia Eagles","WAS":"Washington Football Team","NYG":"New York Giants","GB":"Green Bay Packers","CHI":"Chicago Bears","MIN":"Minnesota Vikings","DET":"Detroit Lions","NO":"New Orleans","CAR":"Carolina Panthers","ATL":"Atlanta Falcons","TB":"Tampa Bay Buccaneers","SEA":"Seattle Seahawks","SF":"San Francisco 49ers","LA":"Los Angeles Rams","ARI":"Arizona Cardinals","NE":"New England Patriots","MIA":"Miami Dolphins","BUF":"Buffalo Bills","NYJ":"New York Jets","CIN":"Cincinnati Bengals","BAL":"Baltimore Ravens","PIT":"Pittsburgh Steelers","CLE":"Cleveland Browns","TEN":"Tennessee Titans","IND":"Indianapolis Colts","JAC":"Jacksonville Jaguars","HOU":"Houston Texans","DEN":"Denver Broncos","LAC":"Los Angeles Chargers","LV":"Las Vegas Raiders","KC":"Kansas City Chiefs","OAK":"Oakland Raiders","SD":"San Diego Chargers","STL":"St Louis Rams"}
      rankings.push(<tr><td>{rank_num}.</td> <td>{team_key[team]}</td><td>{(data['ranks'][i][1]).toFixed(1)}</td></tr>);
      rank_num++;
    }
    let methodology = [<div class="methodology"><b>Methodology:</b> The rankings are calculated by giving each team a rating for a game by taking the rating of the opponent and adding or subtracting the square root of the margin of victory or defeat, and multiplying by 10 simply to give more spaced out ratings. The ratings of a team's games over the whole season are then averaged together to give the team an overall rating. All teams start with a rating 50, and successive iterations of the formula using the ratings from the previous iteration are run until the teams' ratings converges on a single set of numbers.</div>];
    let projections = [<div><br/><h2>Projections for Next Week</h2><br/></div>];
    for (let m in data['projections']) {
      let proj_game = data['projections'][m];
      projections.push(<div><div>{proj_game['winner']} over {proj_game['loser']} by {proj_game['expected_diff']}<br/></div><br/></div>);
      console.log(proj_game);
    }
  return (<div><br/><br/><div class="rankings"><br/><h1>NFL Rankings</h1><h3>Week 11</h3><table class="rankings-table">{rankings}</table><br/>{methodology}<br/></div><br/><br/><div class="projections">{projections}<br/></div><br/><br/></div>);
  }
}

ReactDOM.render(
  <Main />,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
