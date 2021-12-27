import React, { Component } from "react";
import AddTrackPage from "./AddTrackPage";
import ViewTrackPage from "./ViewTrackPage";
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route exact path='/'>
                    <p>This is the home page!</p>
                    </Route>
                    <Route path='/view' component={ViewTrackPage} />
                    <Route path='/add' component={AddTrackPage} />
                </Routes>
            </Router> 
        );
    }
}