import React, {Component} from 'react';

import SpotPlayer from "./Components/SpotPlayer/SpotPlayer";
import music from './Media/烟把儿 - 纸短情长（完整版）.mp3'

import Header from "./Components/Header/Header";
import ControlBar from './Components/ControlBar/ControlBar';

import {BackTop} from 'antd';


import './App.css'


class App extends Component {

    render() {
        return (
            <div>
                <SpotPlayer music={music}/>

                <BackTop/>

                <Header />

                <div className="App-container">
                    <ControlBar/>
                </div>
            </div>
        );
    }
}

export default App;
