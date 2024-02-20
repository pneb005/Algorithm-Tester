import QtQuick 2.15
import QtQuick.Controls.Basic 2.15
import QtQuick.Dialogs

ApplicationWindow {
    id: window
    visible: true
    width: 600
    height: 500
    title: "Algorithm Tester"
    property QtObject backend

    ScrollView {
        id:view
        height: window.height*0.5
        width: window.width*0.5
        x: window.width*0.25
        y: 100
        TextArea {
            objectName: "userInput"
            id: textBox
            placeholderText: ""
            height:view.height
            width:view.width

            background: Rectangle {
                implicitHeight: textBox.height
                implicitWidth: textBox.width
                color: "#DADADA"
            }
        }
    }
    
    FileDialog {
        id: files
        objectName: "filename"
    }

    Button {
        id: fileExplorer
        objectName: "openFiles"
        text: "Open file"
        x: 20
        y: 30
        height: 30 
        width: 70

        background: Rectangle {
            implicitHeight: fileExplorer.height
            implicitWidth: fileExplorer.width
            color:"#DADADA"
        }

        onClicked: files.open()
    }

    Button {
        objectName: "enter"
        font.pixelSize: 24
        text: "Test Speed"
        x: window.width*0.5
        y: window.height*0.8

        background: Rectangle {
            implicitWidth:100
            implicitHeight: 50
            opacity: enabled ? 1 : 0.3
            color: "#DADADA"
        }
    }


    TextArea {
        objectName: "nameCount"
        id: nameCount
        placeholderText:"Number of names"
        placeholderTextColor: "black"
        x: window.width*0.20
        y: window.height*0.75
        background: Rectangle {
            color: "#DADADA"
        }
    }

    TextArea {
        objectName: "loopCount"
        id: loopCount
        placeholderText: "Number of loops"
        placeholderTextColor: "black"
        x: window.width*0.20
        y: window.height*0.85
        background: Rectangle {
            color: "#DADADA"
        }

    }

    Label {
        objectName: "errorLabel"
        id: errorLabel
        text: ""
        color: "red"
        x: window.width*0.50
        y: window.height*0.75
    }

    Connections {
        target: backend
        function onUpdated(msg) {
            textBox.text = msg;
        }

        function onError(msg) {
            errorLabel.text = msg
        }
    }
}