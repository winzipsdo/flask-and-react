import React, {Component} from 'react';
import SpotPlayer from "./SpotPlayer/SpotPlayer";
import music from './Media/烟把儿 - 纸短情长（完整版）.mp3'
import Button from 'antd/lib/button'
import styles from './App.css'


class App extends Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div>
                <SpotPlayer music={music}/>
                <Button type="primary">Button</Button>
            </div>
        );
    }
}

export default App;
