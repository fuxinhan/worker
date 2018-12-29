import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// URL

import axios from 'axios'
import { SERVER_URL } from '../../../utils/config'

// core components
import MyHeader from "../components/MyHeader.jsx";
import Footers from "../components/Footers.jsx";
import ProductDetailsTop from "./compoents/productDetailsTop.jsx";
import ProductDetailsTabs from "./compoents/productDetailsTabs.jsx";

import productStyle from "../../../../assets/jss/material-kit-pro-react/views/productStyle.jsx";


class ProductDetails extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      colorSelect: "0",
      sizeSelect: "0",
      coursesInfoData:''
    };
  }
  componentWillMount() {
    axios.get(`${SERVER_URL}/api/courses/${this.props.match.params.id}/`,{
      headers:{
          Accept: 'application/json'
      }
    }).then((response) => {
        const coursesInfo = response.data
        this.setState({
          coursesInfoData:coursesInfo
        })
        console.log("this is coursesInfoData",this.state.coursesInfoData)
    }).catch((error) => {
        console.log(error.response)
        return Promise.resolve();
    })
  }
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.productPage}>
        <MyHeader></MyHeader>
        <ProductDetailsTop coursesInfoData={this.state.coursesInfoData}/>
        <div className={classNames(classes.section, classes.sectionGray)}>
          <div className={classes.container}>
            <div className={classNames(classes.main, classes.mainRaised)}>
              {console.log(this.props.match.params.id)}
             <ProductDetailsTabs /> 
            </div>
          </div>
        </div>
        <Footers></Footers>
      </div>
    );
  }
}

export default withStyles(productStyle)(ProductDetails);
