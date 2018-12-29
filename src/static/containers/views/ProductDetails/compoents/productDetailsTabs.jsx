import React from "react";

// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";

// @material-ui/icons
import Face from "@material-ui/icons/Face";
import Label from "@material-ui/icons/Label";
import Chat from "@material-ui/icons/Chat";
import Build from "@material-ui/icons/Build";
import BookmarkBorder from "@material-ui/icons/BookmarkBorder";
// core components
import SectionComment from "./sectionComments.jsx";
import ProductCards from "./productCards.jsx";
import GridContainer from "../../../../components/Grid/GridContainer.jsx";
import GridItem from "../../../../components/Grid/GridItem.jsx";
import CustomTabs from "../../../../components/CustomTabs/CustomTabs.jsx";
import tabsStyle from "../../../../../assets/jss/material-kit-pro-react/views/componentsSections/tabsStyle.jsx";
import Info from "../../../../components/Typography/Info.jsx";
import ProductPage from "./productPage";
import ProductDay from "./productDay"
import ProductInfoVideo from "./productInfoVideo"
import ProductVip from './productVip'
import ProductCard from './productCard'

const cart =[];
class SectionTabs extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      stareCart : [
        {
          url:"/static/images/color1.jpg",
          title:"第一章节",
          text:"带你入门python，开始python之旅，从小游戏开始。"
        },
        {
          url:"/static/images/color2.jpg",
          title:"第一章节",
          text:"带你入门python，开始python之旅，从小游戏开始。"
        },
        {
          url:"/static/images/color3.jpg",
          title:"第一章节",
          text:"带你入门python，开始python之旅，从小游戏开始。"
        },
        {
          url:"/static/images/color4.jpg",
          title:"第一章节",
          text:"带你入门python，开始python之旅，从小游戏开始。"
        }
      ]
    }
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.section}>
        <div className={classes.container}>
          <div id="nav-tabs">
            <GridContainer>
              <GridItem xs={12} sm={12} md={12}>
                <CustomTabs
                  headerColor="primary"
                  tabs={[
                    {
                      tabName:"课程细节",
                      tabIcon:Chat,
                      tabContent:(
                        <div>
                          <ProductInfoVideo/>
                          <ProductPage/>
                          <ProductVip/>
                          <ProductDay/>
                          <ProductCards/>
                        </div>
                      )
                    },
                    {
                      tabName: "课程章节",
                      tabIcon: Face,
                      tabContent: (
                        <div>
                          <Label className={classes.iconLeft} />
                          <div className={classes.tabsLHM}>
                            <h4>第一章 课程介绍</h4>
                            <p>介绍课程目标、通过课程能学习到的内容、和系统开发前需要具备的知识</p>
                            <ul className={classes.tabsMT}>
                              <BookmarkBorder className={classes.iconSmall}/>
                              <li>1-1 python分布式爬虫打造搜索引擎简介</li>
                            </ul>
                          </div>

                          <Label className={classes.iconLeft} />
                          <div className={classes.tabsLHM}>
                            <h4>第二章 课程介绍</h4>
                            <p>介绍课程目标、通过课程能学习到的内容、和系统开发前需要具备的知识</p>
                            <ul className={classes.tabsMT}>
                              <BookmarkBorder className={classes.iconSmall}/>
                              <li>2-1 python分布式爬虫打造搜索引擎简介</li>
                            </ul>
                            <ul className={classes.tabsMT}>
                              <BookmarkBorder className={classes.iconSmall}/>
                              <li>2-2 python分布式爬虫打造搜索引擎简介</li>
                            </ul>
                          </div>
                        </div>
                        
                      )
                    },
                    {
                      tabName: "用户评价",
                      tabIcon: Chat,
                      tabContent: (
                        <SectionComment/>
                      )
                    },
                    {
                      tabName: "卡片章节",
                      tabIcon: Face,
                      tabContent:(
                        // <div>
                        //   {cart} 
                        // </div>
                        <ProductCard stareCart={this.state.stareCart}/>
                      )
                    }
                  ]}
                />
              </GridItem>
            </GridContainer>
          </div>
        </div>
      </div>
    );
  }
}

export default withStyles(tabsStyle)(SectionTabs);
