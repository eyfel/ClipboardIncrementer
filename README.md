# CopyPaster

CopyPaster is an advanced tool designed to streamline the copy-paste process for users engaged in tasks that require the frequent copying of predefined values. By displaying an identifier (`copy_id`) and automatically copying its corresponding value (`copy_value`) to the clipboard, it significantly enhances efficiency and accuracy in data entry and documentation processes.

## Key Features

- **Automated Clipboard Copying:** Upon each `Ctrl+V` trigger, automatically copies the next value (`copy_value`) in the list to the clipboard, reducing manual copying errors.
- **Visual Identifier Display:** Shows the `copy_id` in a prominently displayed GUI window, allowing users to visually confirm the data being copied.
- **Streamlined Workflow:** Optimizes repetitive data entry tasks by combining visual cues with automatic clipboard management.
- **User-centric Design:** Features a topmost window with large, bold, red font for easy visibility, ensuring the `copy_id` is always in view.

## Usage Guide

1. Launch the script by executing `python copy_paster.py` in your command line or terminal.
2. The application window will display the `copy_id`, and the associated `copy_value` will be ready for pasting with `Ctrl+V`.
3. The script concludes automatically after the last item in the list has been processed, displaying a message that all items have been displayed.

## Customization

Modify the `copy_list` within the script to include your specific identifiers (`copy_id`) and values (`copy_value`), tailoring the tool to meet your unique requirements.

## Dependencies

Ensure the following dependencies are installed in your Python environment:
- pyperclip
- keyboard

## Contributing

Contributions are welcome! Feel free to fork this repository, propose changes, or suggest new features by submitting pull requests or opening issues.

