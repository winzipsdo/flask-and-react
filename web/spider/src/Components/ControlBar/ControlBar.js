import React, {Component} from 'react';
import './ControlBar.css';

import {Select, DatePicker, Button, Switch} from 'antd';


export default class ControlBar extends Component {
    constructor(props) {
        super(props);

        const curDate = new Date();
        const date_y = curDate.getYear() + 1900;
        const date_M = curDate.getMonth() + 1;
        const date_d = curDate.getDate();

        this.state = {
            site: 'JP',
            date: date_y + '-' + date_M + '-' + date_d
        };

        this.handleGet = this.handleGet.bind(this);
        this.handleSiteChange = this.handleSiteChange.bind(this);
        this.handleDateChange = this.handleDateChange.bind(this);
        this.handleVisualizeChange = this.handleVisualizeChange.bind(this);
    }

    handleGet(){
        const {site,date} = this.state;
        this.props.handleSearch(site,date);
    }

    handleVisualizeChange(checked){
        this.props.handleSwitch(checked);
    }

    handleSiteChange(value) {
        this.setState({
            site: value
        });
    }

    handleDateChange(date, dateString) {
        this.setState({
            date: dateString
        });
    }

    render() {
        const Option = Select.Option;
        const {handleGet, handleSiteChange, handleDateChange, handleVisualizeChange} = this;

        return (
            <div className="ControlBar-container">

                <Select placeholder="Select site"
                        style={{width: 120}}
                        onChange={handleSiteChange}>
                    <Option value="JP">Japan</Option>
                    <Option value="KR">Korea</Option>
                    <Option value="MY">Malaysia</Option>
                    <Option value="TW">Taiwan</Option>
                </Select>

                <DatePicker placeholder="Select date"
                            style={{width: 140}}
                            onChange={handleDateChange} />

                <Switch onChange={handleVisualizeChange} />

                <Button type="primary"
                        onClick={handleGet}>
                    Get
                </Button>

            </div>
        )
    }
}

ControlBar.defaultProps = {
    handleSearch: f => f,
    handleSwitch: f => f
};