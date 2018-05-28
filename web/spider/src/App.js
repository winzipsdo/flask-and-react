import React, {Component} from 'react';

import SpotPlayer from "./Components/SpotPlayer/SpotPlayer";
import music from './Media/烟把儿 - 纸短情长（完整版）.mp3'

import Header from "./Components/Header/Header";
import ControlBar from './Components/ControlBar/ControlBar';
import MsgDisplay from './Components/MsgDisplay/MsgDisplay';

import data_test from './Data';

import {BackTop} from 'antd';


import './App.css'


class App extends Component {
    constructor(props) {
        super(props);
        const curDate = new Date();
        this.state = {
            data: [],
            data_test: data_test,
            loading: false,
        };

        this.add_row = this.add_row.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
    }

    handleSearch(site, date) {
        this.setState({
            loading: true,
            data: []
        },()=>{
            let data = new FormData();
            data.append("site",site);
            data.append("date",date);

            let xhr = new XMLHttpRequest();
            xhr.open("POST", "/api/test", true);
            xhr.onreadystatechange = () => {
                if (xhr.status === 200 && xhr.readyState === 4){
                    const responseJSON = JSON.parse(xhr.responseText);
                    for (let i in responseJSON){
                        const item = responseJSON[i];
                        const row = {
                            key: item['id'],
                            img_url: item['image_url'],
                            name: item['name'],
                            price: item['price'],
                            article_number: item['article_number'],
                            url: item['url'],
                            description: item['description'],
                            spliter: item['spliter'],
                            brand: item['brand'],
                            series: item['series'],
                            site: item['site'],
                            language: item['language'],
                            date: item['date']
                        };
                        this.add_row(row);
                    }
                    this.setState({loading:false});
                }
            };
            xhr.send(data);
        });
    }

    add_row(row) {
        let {data} = this.state;
        data.push(row);
        this.setState({data: data});
    }

    render() {
        const {handleSearch} = this;
        const {data, data_test, loading} = this.state;

        return (
            <div>
                <SpotPlayer music={music}/>

                <BackTop/>

                <Header handleClick={this.add_row}/>

                <div className="App-container">
                    <ControlBar handleSearch={handleSearch}/>
                    <MsgDisplay data={data_test} loading={loading}/>
                </div>
            </div>
        );
    }
}

export default App;
