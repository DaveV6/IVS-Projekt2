buttonBasic = """
    QPushButton {
        border: 1px solid black;
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                          stop:0 #3f3f3f, stop:1 #5f5f5f);
        color: white;
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 24px;
        opacity: 0.8;
    }

    QPushButton:hover {
        background-color: #6f6f6f;
    }

    QPushButton:pressed {
        background-color: #4f4f4f;
    }
""" 



buttonPurple = """
QPushButton {
    border: 2px solid rgba(255, 255, 255, 0.8);
    background-color: radial-gradient(circle at 12.3% 19.3%, rgb(85, 88, 218) 0%, rgb(95, 209, 249) 100.2%);
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
    font-size: 20px;
    opacity: 0.8;
}

QPushButton:hover {
    background-color: #453a57;
}

QPushButton:pressed {
    background-color: #2e2641;
}
"""


buttonDarkGreen = """
    QPushButton {
        border: 1px solid black;
        background-color: #a9c52f;
        color: white;
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 24px;
        opacity: 0.8;
    }

    QPushButton:hover {
        background-color: #6f6f6f;
    }

    QPushButton:pressed {
        background-color: #4f4f4f;
    }
""" 