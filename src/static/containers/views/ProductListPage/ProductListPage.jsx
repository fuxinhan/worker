import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
import axios from 'axios'
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import GridContainer from "../../../components/Grid/GridContainer.jsx";
import Myheader from '../components/MyHeader.jsx';
import Footers from '../components/Footers.jsx';
import ProductTop from './compoents/productTop.jsx';
import ProductTeachers from './compoents/productTeachers.jsx';
import ProductPreFooter from './compoents/productPreFooter.jsx';
import ProductServices from './compoents/productServices.jsx';
import ProductTab from './compoents/productTab.jsx';
import styles from "../../../../assets/jss/material-kit-pro-react/views/ecommerceSections/latestOffersStyle.jsx";
import SingleItem from './compoents/SingleItem.jsx'
import { SERVER_URL } from '../../../utils/config'

// pt 课件数组 Teachers 老师数据   为了简化代码。
class SectionLatestOffers extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            resultsData:''
        }
    }
    componentWillMount() {
        axios.get(`${SERVER_URL}/api/courses/`,{
            headers:{
                Accept: 'application/json'
            }
        }).then((response) => {
            const results = response.data.results
           
            this.setState({
                resultsData:results
            })
            console.log("this is courses",this.state.resultsData)
            return response
        }).catch((error) => {
            console.log(error.response)
            return Promise.resolve();
        })
    }
    
    render() {
    const { classes, data, isFetching, ...rest } = this.props;   

    return (
        <div className={classes.section}>
            <Myheader></Myheader>
            <ProductTop></ProductTop>
            <div className={classes.container}>
                <div className={classNames(classes.main,classes.mainRaised)}>
                    <div className={classes.divHW}>
                        <span className={classes.spanQian}>硬件</span>
                        <span className={classes.spanZh}>|</span>
                        <span className={classes.spanHou}>
                            cong ji chu kai shi rang hai zi liao jie bian cheng
                        </span>
                        {/* <button onClick={getUserDataFetch(token)}>this is token</button> */}
                    </div>

                    { this.state.resultsData!=''?<SingleItem resultsData={this.state.resultsData}/>:<div/> }

                    {/* 软件课程组件 */}
                    <div className={classes.divHW}>
                        <span className={classes.spanQian}>软件</span>
                        <span className={classes.spanZh}>|</span>
                        <span className={classes.spanHou}>
                            cong ji chu kai shi rang hai zi liao jie bian cheng
                        </span>
                    </div>
                    {/* <SingleItem resultsData={this.state.resultsData}/> */}

                    {/* 硬件和软件课程组件 */}
                    <div className={classes.divHW}>
                        <span className={classes.spanQian}>软件 + 硬件</span>
                        <span className={classes.spanZh}>|</span>
                        <span className={classes.spanHou}>
                            cong ji chu kai shi rang hai zi liao jie bian cheng
                        </span>
                    </div>
                    {/* <SingleItem resultsData={this.state.resultsData}/> */}

                    {/* 精英名师组件 */}
                    <div className={classes.divHW}>
                        <span className={classes.spanQian}>瓦力精英名师</span>
                        <span className={classes.spanZh}>|</span>
                        <span className={classes.spanHou}>
                            cong ji chu kai shi rang hai zi liao jie bian cheng
                        </span>
                    </div>
                    <GridContainer>
                        <ProductTeachers/>
                    </GridContainer>

                    {/* 课程与服务组件 */}
                    <div className={classes.divHW}>
                        <span className={classes.spanQian}>课程与服务</span>
                        <span className={classes.spanZh}>|</span>
                        <span className={classes.spanHou}>
                            cong ji chu kai shi rang hai zi liao jie bian cheng
                        </span>
                    </div>
                    <ProductServices/>

                    {/* 加盟商服务组件 */}
                    <ProductTab/>
                </div>
            </div>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <div>
                <ProductPreFooter/>
                <Footers></Footers>
            </div>
            
        </div>
    )}
};

export default withStyles(styles)(SectionLatestOffers);
