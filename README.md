# Shakespearean Sonnet Poem Generator

Welcome to the Shakespearean Sonnet Poem Generator! This project utilizes the GPT-2-simple model to generate poems in the style of Shakespeare's sonnets. 
With the integration of tkinter, a Python GUI toolkit, the generator provides a user-friendly interface for generating custom sonnets.

### Objectives

The primary objectives of this project are as follows:

- Develop a poem generator that emulates the style and language of Shakespeare's sonnets.
- Utilize GPT-2 model for generating authentic-sounding Shakespearean sonnets.
- Create a user-friendly interface using tkinter for easy interaction with the generator.

### Built With

- GPT-2 Model - [OpenAI](https://openai.com/)
- Python GUI Toolkit - [Tkinter](https://docs.python.org/3/library/tk.html)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/cosettekay/Sonnet_Generator.git
    ```

2. Install the required dependencies:

    ```bash
    pip install gpt-2-simple tkinter jupyter tensorflow numpy
    ```

## Usage

1. **Install Dependencies**: Ensure you have installed the required dependencies by running the following commands above under Installation. Note that using jupyter notebooks is not required. 
The code provided in the gpt2-poet.ipynb file is written in a Jupyter Notebook format, but you can also run it in any Python environment capable of running Jupyter notebooks or Python scripts.

2. **Download and Fine-Tune GPT-2 Model**: Execute the code within the `gpt2-poet.ipynb` file in a Jupyter Notebook environment or any Python environment capable of running Jupyter notebooks. 
This notebook downloads the GPT-2 model, fine-tunes it on the provided Shakespeare's sonnets dataset, and saves the fine-tuned model checkpoints. Adjust file paths as 
necessary before running the code. You may also freely use other datasets to train and finetune your model, adhering to your preferred poem format and style.

3. **Set Up the Frontend**: Ensure you have `app.py` and the fine-tuned model checkpoints available in the correct directories. Adjust the `checkpoint_dir` and `run_name` 
variables in `app.py` according to your file structure.

4. **Run the Application**: Execute the `app.py` file in a Python environment. This will launch a tkinter GUI window where you can input prompts and generate sonnets based on 
the fine-tuned GPT-2 model.

5. **Generate Sonnets**: Enter a prompt in the input field provided and click the "Generate Poem" button. The generated sonnet will appear in the output text area below.

6. **Customization (Optional)**: Feel free to adjust the parameters used for generating sonnets in the `generate_poem()` function within `app.py` to fine-tune the output 
according to your preferences.

# Results
Below are the results of my own finetuned model: 

<img width="386" alt="ML #1" src="https://github.com/cosettekay/Sonnet_Generator/assets/71306558/75432433-eff4-456a-b6b2-389e9190e16f">

<img width="386" alt="ML #2" src="https://github.com/cosettekay/Sonnet_Generator/assets/71306558/95bf99ab-4772-4853-97a6-b645ffce357f">

<img width="386" alt="ML #3" src="https://github.com/cosettekay/Sonnet_Generator/assets/71306558/5243c961-a1d9-43af-830c-ef459b974221">

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or would like to contribute enhancements, please submit a pull request.

## Acknowledgments

- GPT-2-simple: [GitHub](https://github.com/minimaxir/gpt-2-simple)
- Shakespeare's Sonnets Dataset: [Github](https://github.com/enerrio/Generate-Shakespeare-Sonnets/blob/master/sonnets.txt)
- Tkinter: [Python Documentation](https://docs.python.org/3/library/tk.html)

