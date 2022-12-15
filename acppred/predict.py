from acppred.models import Model
from argparse import ArgumentParser
from Bio import SeqIO
import pandas as pd

def main():

    argument_parser = ArgumentParser(description='predicts anticencer peptides in a FASTA file')
    argument_parser.add_argument('--input', required=True, help='input fasta file')
    argument_parser.add_argument('--output', required=True, help='output csv file')
    argument_parser.add_argument('--model', required=True, help='pre-trained ACPPred model')

    arguments = argument_parser.parse_args()


    model = Model.load(arguments.model)

    predictions = []

    for sequence_record in SeqIO.parse(arguments.input, 'fasta'):
        sequence = str(sequence_record.seq)
        prediction = model.predict(sequence)
        sequence_data = {'sequence_id': sequence_record.id, 'prediction': prediction}
        predictions.append(sequence_data)

    df_predictions = pd.DataFrame(predictions, columns=['sequence_id', 'prediction']) 
    df_predictions.to_csv(arguments.output, index=False)

if __name__ == '__main__':
    main()