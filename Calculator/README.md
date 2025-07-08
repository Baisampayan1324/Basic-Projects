# Scientific Calculator

A feature-rich scientific calculator built with Python and Tkinter, offering a modern dark theme interface with comprehensive mathematical functions.

## Features

### 🧮 **Basic Operations**
- Addition, subtraction, multiplication, division
- Decimal point support
- Clear (AC) and Delete (DEL) functions
- Keyboard input support

### 🔬 **Scientific Functions**
- **Trigonometric Functions**: sin, cos, tan, cot (in degrees)
- **Logarithmic Functions**: log (base 10), ln (natural log)
- **Exponential Functions**: e^x, 10^x
- **Power Functions**: x², x³, x^n, x⁻¹
- **Root Functions**: √ (square root), ∛ (cube root), ⁿ√ (nth root)
- **Special Constants**: π (pi), e (Euler's number)
- **Other Functions**: abs, factorial, modulo, integer division

### 🎨 **User Interface**
- Modern dark theme with cyan accents
- Responsive grid layout
- Professional button styling
- Large, readable display
- Keyboard shortcuts support

### ⌨️ **Keyboard Shortcuts**
- **Numbers (0-9)**: Direct input
- **Operators**: +, -, *, /, (, )
- **Enter**: Calculate result
- **Backspace**: Delete last character
- **C**: Clear all

## Screenshots

The calculator features a sleek dark interface with:
- Dark background (#121212)
- Cyan display text (#0ef)
- Color-coded buttons:
  - Scientific functions: Blue (#3f51b5)
  - Numbers: Dark gray (#333)
  - Operators: Teal (#00897b)
  - Special functions: Red (#b71c1c)

## Installation

### Prerequisites
- Python 3.x
- Tkinter (usually comes with Python)

### Setup
1. Clone or download the project
2. Navigate to the project directory
3. Run the calculator:
```bash
python main.py
```

## Usage

### Basic Calculations
1. Click number buttons or type on keyboard
2. Use operator buttons (+, -, ×, ÷)
3. Press = or Enter to calculate

### Scientific Functions
1. Enter a number
2. Click the desired scientific function button
3. The result will be displayed immediately

### Examples
- **Basic**: `2 + 3 = 5`
- **Scientific**: `sin(30) = 0.5`
- **Power**: `2^3 = 8`
- **Root**: `√16 = 4`

## File Structure

```
Calculator/
├── main.py          # Main calculator application
└── README.md        # This file
```

## Technical Details

### Dependencies
- `tkinter`: GUI framework
- `math`: Mathematical functions
- Built-in Python libraries only

### Architecture
- **Global State Management**: Uses global variables for calculator state
- **Event-Driven Design**: Button clicks and keyboard events
- **Modular Functions**: Each operation is a separate function
- **Error Handling**: Try-catch blocks for invalid operations

### Key Functions
- `button_click()`: Adds characters to display
- `button_equal()`: Evaluates expressions
- `trig_sin/cos/tan()`: Trigonometric calculations
- `square_root()`, `third_root()`: Root calculations
- `factorial()`: Recursive factorial implementation
- `key_press()`: Keyboard event handling

## Customization

### Theme Colors
You can modify the color scheme by changing these variables:
```python
# Background colors
bg_color = "#121212"
display_bg = "#1f1f1f"
display_fg = "#0ef"

# Button colors
sci_color = "#3f51b5"    # Scientific functions
num_color = "#333"       # Numbers
op_color = "#00897b"     # Operators
special_color = "#b71c1c" # Special functions
```

### Window Size
Adjust the window dimensions:
```python
tk_calc.geometry("480x700")  # Width x Height
```

## Error Handling

The calculator handles various error conditions:
- Invalid mathematical expressions
- Division by zero
- Negative numbers for square root
- Invalid input for functions

All errors display "ERROR" in the display.

## Contributing

Feel free to contribute by:
- Adding new mathematical functions
- Improving the UI design
- Adding unit tests
- Fixing bugs
- Adding new features

## License

This project is open source and available under the MIT License.

## Future Enhancements

Potential improvements:
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] History of calculations
- [ ] Unit conversions
- [ ] Graphing capabilities
- [ ] Programmer mode
- [ ] Statistics functions
- [ ] Save/load calculations
- [ ] Multiple themes

## Support

If you encounter any issues or have questions:
1. Check the error messages in the display
2. Ensure you're using valid mathematical expressions
3. Verify Python and Tkinter are properly installed

---

**Enjoy calculating! 🧮✨** 