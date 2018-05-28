import React, {Component} from 'react';
import './MsgDisplay.css';

import {Table} from 'antd';

export default class MsgDisplay extends Component {
    constructor(props) {
        super(props);

        const columns = [
            {
                title: 'Image',
                width: 120,
                dataIndex: 'img_url',
                key: 'img_url',
                render: (text)=>(
                    <a href={text} target="_blank">
                        <img style={{width:'60px'}} src={text}/>
                    </a>

                ),
            }, {
                title: 'Name',
                width: 80,
                dataIndex: 'name',
                key: 'name',
                render: text=>(
                    <div style={{
                        fontWeight: 'bold'
                    }}>{text}</div>
                )
            }, {
                title: 'Price',
                width: 200,
                dataIndex: 'price',
                key: 'price',
                sorter: (a,b) => a.price - b.price
            }, {
                title: 'Article Number',
                width: 200,
                dataIndex: 'article_number',
                key: 'article_number'
            },  {
                title: 'Spliter',
                width: 100,
                dataIndex: 'spliter',
                key: 'spliter',
                sorter: (a,b) => a.spliter.length - b.spliter.length
            }, {
                title: 'Brand',
                width: 100,
                dataIndex: 'brand',
                key: 'brand',
                sorter: (a,b) => a.brand.length - b.brand.length
            }, {
                title: 'Series',
                width: 100,
                dataIndex: 'series',
                key: 'series',
                sorter: (a,b) => a.series.length - b.series.length
            }, {
                title: 'URL',
                width: 100,
                dataIndex: 'url',
                key: 'url',
                render: text => (
                    <a target="_blank" href={text}>Click</a>
                )
            },{
                title: 'Site',
                width: 100,
                dataIndex: 'site',
                key: 'site',
            }, {
                title: 'Language',
                width: 140,
                dataIndex: 'language',
                key: 'language'
            }, {
                title: 'Date',
                width: 100,
                dataIndex: 'date',
                key: 'date'
            }
        ];

        this.state = {
            columns: columns,
        }
    }

    render() {
        const { data, loading } = this.props;
        const columns = this.state.columns;
        return (
            <div className="MsgDisplay-container">
                <Table dataSource={data}
                       columns={columns}
                       position='top'
                       loading={loading}
                       scroll={{x:true}}
                       expandedRowRender={
                           record => (
                               <p style={{margin:'0',width:'100%'}}>{record.description}</p>
                           )
                       }
                       style={{
                           whiteSpace:'nowrap',
                           textOverflow:'ellipsis'
                       }}
                       pagination={{
                           pageSize: 6,
                           showQuickJumper: true,
                           showTotal: total=>"Total: " + total
                       }}
                />
            </div>
        )
    }
}
