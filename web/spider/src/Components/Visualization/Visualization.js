import React, {Component} from 'react';
import './Visualization.css'

//d3
import * as d3 from 'd3'

export default class Visualization extends Component {
    constructor(props) {
        super(props);
        this.print = this.print.bind(this);
    }

    componentDidMount() {
        this.print();
    }

    print() {
        const {data} = this.props;

        var marge = {top: 100, bottom: 0, left: 0, right: 0};

        var svg = d3.select("svg");
        var width = svg.attr("width");
        var height = svg.attr("height");

        var g = svg.append("g")
            .attr("transform", "translate(" + marge.top + "," + marge.left + ")");

        var scale = svg.append("g")
            .attr("transform", "translate(" + marge.top + "," + marge.left + ")");

        var hierarchyData = d3.hierarchy(data)
            .sum(function (d) {
                return d.value;
            });

        var tree = d3.tree()
            .size([width - 200, height - 200])
            .separation(function (a, b) {
                return (a.parent === b.parent ? 1 : 2) / a.depth;
            });

        var treeData = tree(hierarchyData);

        var nodes = treeData.descendants();
        var links = treeData.links();

        var Bezier_curve_generator = d3.linkHorizontal()
            .x(function (d) {
                return d.y;
            })
            .y(function (d) {
                return d.x;
            });

        g.append("g")
            .selectAll("path")
            .data(links)
            .enter()
            .append("path")
            .attr("d", function (d) {
                var start = {x: d.source.x, y: d.source.y};
                var end = {x: d.target.x, y: d.target.y};
                return Bezier_curve_generator({source: start, target: end});
            })
            .attr("fill", "none")
            .attr("stroke", "#ADABAE")
            .attr("stroke-width", 0.5);//retina

        var gs = g.append("g")
            .selectAll("g")
            .data(nodes)
            .enter()
            .append("g")
            .attr("transform", function (d) {
                var cx = d.x;
                var cy = d.y;
                return "translate(" + cy + "," + cx + ")";
            });

        gs.append("circle")
            .attr("r", 6)
            .attr("fill", "white")
            .attr("stroke", "#84B6ED")
            .attr("stroke-width", 1);

        //文字
        gs.append("text")
            .attr("x", function (d) {
                return d.children ? -40 : 8;
            })
            .attr("y", -5)
            .attr("dy", 10)
            .text(function (d) {
                return d.data.name;
            })
    }

    render() {

        return (
            <div className="Visualization-container">
                <svg width="1400" height="1200"/>
            </div>

        );
    }
}

Visualization.defaultProps = {
    data: []
};