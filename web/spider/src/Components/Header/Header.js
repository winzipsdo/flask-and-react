import "./Header.css"
import React, { Component } from 'react';

export default class Header extends Component{

    render(){
        const {handleClick} = this.props;

        return (
            <div className="Header-container">
                <div className="Header-logo-wrapper">
                    <div className="Header-logo"/>
                    <div className="Header-title"
                         onClick={handleClick}>
                        Larva
                    </div>
                </div>
            </div>
        )
    }
}

Header.defaultProps = {
    handleClick: ()=>{
        alert("ok");
    },
};
