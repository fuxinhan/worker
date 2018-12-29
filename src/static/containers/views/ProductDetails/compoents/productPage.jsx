import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// @material-ui/icons
import LocalShipping from "@material-ui/icons/LocalShipping";
import VerifiedUser from "@material-ui/icons/VerifiedUser";
import Favorite from "@material-ui/icons/Favorite";
// core components
import GridContainer from "../../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../../components/Grid/GridItem.jsx";
import InfoArea from "../../../../components/InfoArea/InfoArea.jsx";

import productStyle from "../../../../../assets/jss/material-kit-pro-react/views/productStyle.jsx";

class ProductPage extends React.Component {

    render() {
        const { classes } = this.props;
        return (
            <div className={classNames(classes.features, classes.textCenter,classes.lineHeight)}>
              <h3>让你比自学更快的Python视频教程 </h3>
              <span>职场竞争如此激烈，时间浪费不得，名师指导让你学的更快、更好、更扎实</span>
              <GridContainer>
                <GridItem md={4} sm={4}>
                  <InfoArea
                    title="名师亲授"
                    description="讲师有八年开发经验更理解你学习新语言的痛点"
                    icon={LocalShipping}
                    iconColor="info"
                    vertical
                  />
                </GridItem>
                <GridItem md={4} sm={4}>
                  <InfoArea
                    title="结合生活"
                    description="从实际工作角度讲解语法应用

                    让你更容易上手实际开发和生活相关的案例"
                    icon={VerifiedUser}
                    iconColor="success"
                    vertical
                  />
                </GridItem>
                <GridItem md={4} sm={4}>
                  <InfoArea
                    title="学练结合"
                    description="课程讲解过程将穿插相应语法练习题目

                    让你学以致用，更扎实的掌握知识"
                    icon={Favorite}
                    iconColor="rose"
                    vertical
                  />
                </GridItem>
              </GridContainer>

            </div>
        )
    }

}

export default withStyles(productStyle)(ProductPage);