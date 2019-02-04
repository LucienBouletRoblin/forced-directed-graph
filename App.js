import React from "react";
import "./App.css";
import { dataNameColor } from "./dataJson";
import { Graph } from "react-d3-graph";

const myConfig = {
  nodeHighlightBehavior: true,
  width: 800,
  height: 800,
  node: {
    size: 120,
    highlightStrokeColor: "blue"
  },
  link: {
    highlightColor: "lightblue"
  }
};

class App extends React.Component {
  // graph event callbacks
  onClickNode = function(nodeId) {
    window.alert(`Clicked node ${nodeId}`);
  };

  onClickLink = function(source, target) {
    window.alert(`Clicked link between ${source} and ${target}`);
  };

  render() {
    let array2 = [...Array(300)].map((_, i) => ({
      degree: 1,
      eigenvector: 0.0022204916389402633,
      id: i && "" + i,
      color: "lightblue"
    }));
    let array3 = dataNameColor.nodes.concat(array2);
    dataNameColor.nodes = array3;
    return (
      <div style={{ border: "1px solid black" }}>
        <h1> Graph test: {dataNameColor.nodes.length} peoples</h1>
        <Graph
          id="graph-name-color" // id is mandatory, if no id is defined rd3g will throw an error
          data={dataNameColor}
          config={myConfig}
          onClickNode={this.onClickNode}
          onClickLink={this.onClickLink}
        />
      </div>
    );
  }
}

export default App;
