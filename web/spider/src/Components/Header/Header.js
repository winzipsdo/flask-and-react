import "./Header.css"
import React, { Component } from 'react';

export default class Header extends Component{
    constructor(props){
        super(props);
        this.HandleClick = this.HandleClick.bind(this);
    }

    HandleClick(e){
        alert("Larva");
    }

    render(){
        return (
            <div className="Header-container">
                <div className="Header-logo-wrapper">
                    <div className="Header-logo"/>
                    <div className="Header-title"
                         onClick={this.HandleClick}>
                        Larva
                    </div>
                </div>
            </div>
        )
    }
}
