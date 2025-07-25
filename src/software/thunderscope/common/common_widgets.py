from pyqtgraph.Qt import QtCore
from pyqtgraph.Qt.QtWidgets import *
from pyqtgraph.Qt.QtCore import *
from software.py_constants import *
from software.thunderscope.util import color_from_gradient


class FloatSlider(QSlider):
    """This class extends QSlider to offer support to float values instead of just ints"""

    floatValueChanged = pyqtSignal(float)

    def __init__(self, decimals: int = 1, *args, **kwargs):
        """Creates a FloatSlider with the given number of decimal places

        :param decimals: number of decimal places that value of slider should have
        """
        super(FloatSlider, self).__init__(*args, **kwargs)
        self.decimals = 10**decimals

        # slider now emits a float value signal every time its value changes
        self.valueChanged.connect(self.emitFloatValueChanged)

    def emitFloatValueChanged(self) -> None:
        """Emits a signal with the slider's float value"""
        self.floatValueChanged.emit(self.value())

    def value(self) -> float:
        """Gets the actual value of the slider and converts it to the float value
        of corresponding decimal places

        :return: the float value of the slider
        """
        return float(super(FloatSlider, self).value()) / self.decimals

    def setMinimum(self, min_val: float) -> None:
        """Sets a minimum float value for this slider

        :param min_val: value to set as the minimum
        """
        return super(FloatSlider, self).setMinimum(int(min_val * self.decimals))

    def setMaximum(self, max_val: float) -> None:
        """Sets a maximum float value for this slider

        :param max_val: value to set as the maximum
        """
        return super(FloatSlider, self).setMaximum(int(max_val * self.decimals))

    def setValue(self, value: float) -> None:
        """Sets a float value as the value for this slider

        :param value: value to set as the slider's value
        """
        super(FloatSlider, self).setValue(int(value * self.decimals))


class ColorQLabel(QLabel):
    """A QLabel that changes color based on the float value it holds
    Can provide a custom min and max value
    The label starts off with no color and becomes more Red as the value increases up till the max value
    """

    def __init__(
        self,
        label_text: str,
        initial_value: float,
        min_val: float = 0,
        max_val: float = 100,
    ):
        """Initializes the ColorQLabel with the given label, min and max bounds
        Or 0 and 100 as default

        :param label_text: the text displayed within this label as a string
        :param initial_value: the initial value of the label
        :param min_val: the minimum value of the label color (no color)
        :param max_val: the maxmimum value of the label color (100% red)
        """
        super(ColorQLabel, self).__init__()

        self.min = min_val
        self.max = max_val
        self.label_text = label_text

        self.set_float_val(initial_value)

    def set_float_val(self, val: float) -> None:
        """Sets the current value of the label to the given float value

        :param val: the new float value
        """
        self.setText(f"{self.label_text} {val:d}")
        self.__update_background_color(val)

    def __update_background_color(self, val: float) -> None:
        """Converts the given float to an percentage using the current min-max range
        Updates the background color's opacity to be that percentage

        :param val: the float value of the label to update
        """
        percent = max(0, min(float(val - self.min) / (self.max - self.min), 1))

        self.setStyleSheet(f"background: rgba(255, 0, 0, {percent})")


class ColorProgressBar(QProgressBar):
    """This class extends QProgressBar to support floats instead of ints
    Also changes progress bar color based on percentage filled
    """

    floatValueChanged = pyqtSignal(float)

    def __init__(self, min_val: float, max_val: float, decimals: int = 2):
        """Creates a ColorProgressBar with the specified min, max and decimals
        Sets initial slider color to grey

        :param min_val: min value of slider
        :param max_val: max value of slider
        :param decimals: number of decimal places to be used
        """
        super(ColorProgressBar, self).__init__()

        self.decimals = 10**decimals

        super(ColorProgressBar, self).setRange(
            int(min_val * self.decimals), int(max_val * self.decimals)
        )

        super(ColorProgressBar, self).setStyleSheet(
            "QProgressBar::chunk" "{" "background: grey" "color: black" "}"
        )

        self.valueChanged.connect(self.emitFloatValueChanged)

    def emitFloatValueChanged(self) -> None:
        """Emits a signal with the slider's float value"""
        self.floatValueChanged.emit(self.value())

    def setValue(self, value: float) -> None:
        """Sets the value of the slider to the given float value
        Sets the color of the slider based on the percentage filled
            - 100% to 50% -> Green to Yellow
            - 50% to 0% -> Yellow to Red

        :param value: the float value to set
        """
        super(ColorProgressBar, self).setValue(int(value * self.decimals))

        percent = self.getPercentage()
        color = color_from_gradient(
            percent,
            [0, 0.5, 1],
            [255, 200, 0],
            [0, 170, 180],
            [0, 0, 0],
            [255, 255, 255],
        )

        # Extract color into CSS form.
        super(ColorProgressBar, self).setStyleSheet(
            "QProgressBar::chunk"
            "{"
            f"background: rgb({color.red()}, {color.green()}, {color.blue()})"
            "}"
        )

    def getPercentage(self):
        """Gets the current percentage between 0 and 1 from the current value
        Compared to the current min and max
        """
        return min(
            1,
            max(
                0,
                (self.value() - self.minimum()) / (self.maximum() - self.minimum()),
            ),
        )

    def maximum(self) -> float:
        """Gets the maximum value of this progress bar as a float"""
        return float(super(ColorProgressBar, self).maximum()) / self.decimals

    def minimum(self) -> float:
        """Gets the minimum value of this progress bar as a float"""
        return float(super(ColorProgressBar, self).minimum()) / self.decimals

    def value(self) -> float:
        """Gets the current value of this progress bar as a float"""
        return float(super(ColorProgressBar, self).value()) / self.decimals


class ToggleableButton(QPushButton):
    """A QPushButton which can be enabled or disabled
    Indicates with cursor if it is enabled or disabled
    """

    def __init__(self, enabled: bool):
        """Creates a new button with the given state

        :param enabled: the starting state of the button
        """
        super(ToggleableButton, self).__init__()
        self.enabled = enabled

    def toggle_enabled(self, enabled: bool):
        """Toggles the enabled state of the button
        :param enabled: the new enabled state
        """
        self.enabled = enabled

    def enterEvent(self, event) -> None:
        """Sets the cursor to depending on if the button is enabled
        to indicate that this widget is clickable or unclickable

        :param event: the mouse enter event
        """
        self.setCursor(
            QtCore.Qt.CursorShape.PointingHandCursor
            if self.enabled
            else QtCore.Qt.CursorShape.ForbiddenCursor
        )


def create_buttons(text: list):
    """Creates QPushButton objects inside a QGroupBox object.
    The default color of button will be white with black background.

    :param text: type:list - list of text for all buttons
    :return group_box, buttons:
            QGroupBox object - add this to the widget
            list of QPushButton objects - use this to perform tasks on the buttons
    """
    group_box = QGroupBox()
    num_buttons = len(text)
    buttons = []

    for i in range(num_buttons):
        button = QPushButton(text[i])
        buttons.append(button)

    hbox = QHBoxLayout()

    for button in buttons:
        hbox.addWidget(button)
    group_box.setLayout(hbox)

    return group_box, buttons


def create_radio(text: list, radio_group):
    """Creates QRadioButton objects inside a QGroupBox object.
    The default color of button background will be white.

    :param text: - list of text for all buttons
    :param radio_group: QButtonGroup to add these buttons to
    :return group_box, buttons:
                QGroupBox object - add this to the widget
                list of QRadioButton object - use this to perform tasks on the buttons
    """
    group_box = QGroupBox()
    num_buttons = len(text)
    radios = []

    for i in range(num_buttons):
        radio = QRadioButton(text[i])
        # this is so that the button is properly visible in black background
        radio_group.addButton(radio)
        radios.append(radio)

    hbox = QHBoxLayout()

    for radio in radios:
        hbox.addWidget(radio)
    group_box.setLayout(hbox)

    return group_box, radios


def create_slider_abs(slider, text, min_val, max_val, tick_spacing):
    """Set a given QSlider or extended slider inside a QGroupBox object, along with a value
    label on the right. The slider orientation will be horizontal.

    Allows support for classes that extend QSlider to support floats, etc.

    :param slider: slider of type QSlider or a child class of QSlider
    :param text: text to display above the slider
    :param min_val: lowest value of the slider
    :param max_val: highest value of the slider
    :param tick_spacing: interval between two ticks on the slider
    :return vbox, slider, value_label:
            QVBoxLayout object - add this to the widget
            QSlider object - use this to perform tasks on the button
            displays value of slider, update this when value is changed
    """
    slider.setMinimum(min_val)
    slider.setMaximum(max_val)
    slider.setTickPosition(QSlider.TickPosition.NoTicks)
    slider.setTickInterval(tick_spacing)

    vbox = QVBoxLayout()

    if text:
        slider_label = QLabel(str(text))
        vbox.addWidget(slider_label)

    value_label = QLabel(str(slider.value()))
    vbox.addWidget(value_label)
    vbox.addWidget(slider)

    return vbox, slider, value_label


def create_slider(text, min_val, max_val, tick_spacing):
    """Creates a QSlider object and returns a QGroupBox object with the slider and a label

    :param text: text to display above the slider
    :param min_val: lowest value of the slider
    :param max_val: highest value of the slider
    :param tick_spacing: interval between two ticks on the slider
    :return vbox, slider, value_label:
            QVBoxLayout object - add this to the widget
            QSlider object - use this to perform tasks on the button
            displays value of slider, update this when value is changed
    """
    slider = QSlider(Qt.Orientation.Horizontal)

    return create_slider_abs(slider, text, min_val, max_val, tick_spacing)


def create_float_slider(text, decimals, min_val, max_val, tick_spacing):
    """Creates a FloatSlider object and returns a QGroupBox object with the slider and a label

    :param decimals: number of decimals for slider values
    :param text: text to display above the slider
    :param min_val: lowest value of the slider
    :param max_val: highest value of the slider
    :param tick_spacing: interval between two ticks on the slider
    :return vbox, slider, value_label:
            QVBoxLayout object - add this to the widget
            QSlider object - use this to perform tasks on the button
            displays value of slider, update this when value is changed
    """
    slider = FloatSlider(decimals, Qt.Orientation.Horizontal)

    return create_slider_abs(slider, text, min_val, max_val, tick_spacing)


def set_table_data(
    data, table, header_size_hint_width_expansion, item_size_hint_width_expansion
):
    """Set data in a table

    :param data: dict containing {"column_name": [column_items]}
    :param table: table widget that will contain the data
    :param header_size_hint_width_expansion: the factor multiplied by the length of the header
    :param item_size_hint_width_expansion: the factor multiplied by the length of the item
    """
    horizontal_headers = []

    for n, key in enumerate(data.keys()):
        horizontal_headers.append(key)

        for m, item in enumerate(data[key]):
            str_item = str(item)
            newitem = QTableWidgetItem(str_item)
            newitem.setSizeHint(
                QtCore.QSize(
                    max(
                        len(key) * header_size_hint_width_expansion,
                        len(str_item) * item_size_hint_width_expansion,
                    ),
                    1,
                )
            )
            table.setItem(m, n, newitem)

    table.setHorizontalHeaderLabels(horizontal_headers)


def disconnect_signal(signal: QtCore.Signal):
    """Helper function to disconnect all connections for a Qt signal.
    Suppresses TypeErrors thrown by Signal.disconnect() if there are no connections.
    """
    try:
        signal.disconnect()
    except TypeError:
        pass


def enable_button(button):
    """Enables the given button and sets the button UI to reflect that
    visually to the user.

    :param button: button to change the state of
    """
    button.setStyleSheet("")
    button.setEnabled(True)


def disable_button(button):
    """Disables the given button and sets the button UI to reflect that
    visually to the user.

    :param button: button to change the state of
    """
    button.setStyleSheet("background-color: grey")
    button.setEnabled(False)


def disable_slider(slider):
    """Disables a slider by getting the current value and setting the slider to that
    value every time the slider is moved

    This results in slider value not changing even when slider is moved

    :param slider: slider widget to be disabled
    """
    old_val = slider.value()
    slider.sliderMoved.connect(lambda new_val: slider.setValue(old_val))
    slider.setStyleSheet(
        "QSlider::sub-page:horizontal"
        "{"
        "background-color: grey"
        "}"
        "QSlider::handle"
        "{"
        "color: grey;"
        "border-radius: 5px;"
        "}"
    )


def enable_slider(slider):
    """Enables a slider that was disabled with disable_slider

    :param slider: slider widget to be enabled
    """
    disconnect_signal(slider.sliderMoved)
    slider.setStyleSheet("")


def disable_radio_button(button_group):
    """Disables a whole radio button group
    Sets all buttons to unselected and disables their onClick function

    :param button_group: button group to disable
    """
    button_group.setExclusive(False)
    for button in button_group.buttons():
        button.setChecked(False)
        button.clicked.disconnect()
        button.clicked.connect(lambda state, curr=button: curr.setChecked(False))


def draw_robot(painter, rect, start_angle_degree, span_angle_degree):
    """Draws a robot bounded by the given rectangle with a chord defined by the given angles

    :param painter: the QPainter object that is drawing in thunderscope
    :param rect: the rectangle that is bounding the robot's circle
    :param start_angle_degree: the start of the chord, measured anti-clockwise from the horizontal middle in degrees
    :param span_angle_degree: the end of the chord, measured anti-clockwise from the horizontal middle in degrees
    """
    convert_degree = -16

    painter.drawChord(
        rect,
        start_angle_degree * convert_degree,
        span_angle_degree * convert_degree,
    )


def display_tooltip(event, tooltip_text):
    """Checks given event to see if it is an Enter or Leave event
    Upon Enter, displays a tooltip with the given text
    Upon Leave, hides the tooltip

    :param event: event to check
    :param tooltip_text: the text to display in the tooltip
    """
    if str(event.type()) == "Type.Enter":
        QToolTip.showText(
            QPoint(
                int(event.globalPosition().x()),
                int(event.globalPosition().y()),
            ),
            tooltip_text,
            msecShowTime=int(20 * MILLISECONDS_PER_SECOND),
        )
    elif str(event.type()) == "Type.Leave":
        QToolTip.hideText()
