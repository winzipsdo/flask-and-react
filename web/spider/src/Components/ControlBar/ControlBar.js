import React,{Component} from 'react';
import './ControlBar.css';

import {Select, DatePicker, Button} from 'antd';


export default class ControlBar extends Component{
    constructor(props){
        super(props);
        this.handleSiteChange = this.handleSiteChange.bind(this);
        this.handleDateChange = this.handleDateChange.bind(this);
    }

    handleSiteChange(value){
        console.log(value);
    }

    handleDateChange(date, dateString){
        console.log(date);
        console.log(dateString);
    }

    render(){
        const Option = Select.Option;

        return (
            <div className="ControlBar-container">
                <Select placeholder="Select site"
                        style={{ width:120 }}
                        onChange={this.handleSiteChange}>
                    <Option value="JP">Japan</Option>
                    <Option value="KR">Korea</Option>
                    <Option value="MY">Malaysia</Option>
                    <Option value="TW">Taiwan</Option>
                </Select>
                <DatePicker placeholder="Select date"
                            style={{ width:140 }}
                            onChange={this.handleDateChange} />
                <Button type="primary">Get</Button>
            </div>
        )
    }
}