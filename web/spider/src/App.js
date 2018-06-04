import React, {Component} from 'react';

import SpotPlayer from "./Components/SpotPlayer/SpotPlayer";
import music from './Media/烟把儿 - 纸短情长（完整版）.mp3'

import Header from "./Components/Header/Header";
import ControlBar from './Components/ControlBar/ControlBar';
import MsgDisplay from './Components/MsgDisplay/MsgDisplay';
import Visualization from './Components/Visualization/Visualization';

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
            visualize: true
            // visualize: false
        };

        this.add_row = this.add_row.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
        this.handleSwitch = this.handleSwitch.bind(this);
        this.handleTree = this.handleTree.bind(this);
    }

    handleSearch(site, date) {
        this.setState({
            loading: true,
            data: []
        }, () => {
            let data = new FormData();
            data.append("site", site);
            data.append("date", date);

            let xhr = new XMLHttpRequest();
            xhr.open("POST", "/api/test", true);
            xhr.onreadystatechange = () => {
                if (xhr.status === 200 && xhr.readyState === 4) {
                    const responseJSON = JSON.parse(xhr.responseText);
                    for (let i in responseJSON) {
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
                    this.setState({loading: false});
                }
            };
            xhr.send(data);
        });
    }

    handleSwitch(checked) {
        this.setState({visualize:checked});
    }

    add_row(row) {
        let {data} = this.state;
        data.push(row);
        this.setState({data: data});
    }

    handleTree(){
        const data = this.state.data_test;//test line
        // const {data} = this.state;

        function findChild(arr, str) {
            for (let child in arr){
                if (arr[child].name === str){return arr[child];}
            }
            return null;
        }

        let res = {
            "name": "Lenovo",
            "children": []
        };

        for (let item in data){

            let brand = data[item].brand;
            let series = data[item].series;
            let name = data[item].name;

            //brand
            if (findChild(res.children, brand) === null){
                res.children.push({
                    "name": brand,
                    "children": []
                });
            }

            //series
            let obj_brand = findChild(res.children, brand);
            if (findChild(obj_brand.children, series) === null){
                obj_brand.children.push({
                    "name": series,
                    "children": []
                });
            }

            //name
            let obj_series = findChild(obj_brand.children, series);
            if (findChild(obj_series.children, name) === null){
                obj_series.children.push({
                    "name": name
                });
            }
        }
        return res;
        // console.log(JSON.stringify(res));
    }

    render() {
        const {handleSearch, handleSwitch, handleTree} = this;
        const {data, data_test, loading, visualize} = this.state;
        const res = handleTree();
        const msg = visualize ? (
            <Visualization data={res}/>
        ) : (
            <MsgDisplay data={data_test} loading={loading}/>
        );
        return (
            <div>
                <SpotPlayer music={music}/>

                <BackTop/>

                <Header handleClick={this.add_row}/>

                <div className="App-container">
                    <ControlBar handleSearch={handleSearch} handleSwitch={handleSwitch}/>
                    {msg}
                </div>
            </div>
        );
    }
}

export default App;
