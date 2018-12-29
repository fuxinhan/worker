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

class ProductDay extends React.Component {
    render() {
        const { classes } = this.props;
        return (
            <div className={classNames(classes.features, classes.textCenter,classes.lineHeight)}>
              <h3>适合人群 </h3>
              <span>对Python感兴趣的人都可以学习本课程，这是一门真正入门课程，但并不止步于入门将带你从入门向进阶过渡</span>
              <GridContainer>
                <GridItem md={4} sm={4}>
                  <InfoArea
                    title="7——12岁"
                    description="3-14岁连贯11年课程体系480次课，48本教材。

                    经过70个学习中心，60余公立校，1500次教研，20000小时的课程验证。"
                    icon={LocalShipping}
                    iconColor="info"
                    vertical
                  />
                </GridItem>
                <GridItem md={4} sm={4}>
                  <InfoArea
                    title="顶级权威"
                    description="国家社科基金重点课题项目、与中国管理科学研究院机器人教育研究中心、中国电子学会共同进行考级教材编写。"
                    icon={VerifiedUser}
                    iconColor="success"
                    vertical
                  />
                </GridItem>
                <GridItem md={4} sm={4}>
                  <InfoArea
                    title="能力与认知"
                    description="积木对孩子的教育“视觉化、动作化”的方式来锻炼儿童小肌肉群的发展的同时，内容设计语言、数学、科学、社会4个主要领域，通过一个主题的搭建，培养孩子主动探索，乐于分享的科学等"
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

export default withStyles(productStyle)(ProductDay);