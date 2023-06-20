
from feature_extraction.n_bytes_per_packet import NBytesPerPacket
from nfstream import NFStreamer  # https://www.nfstream.org/docs/api
import os

input_dir = '/mnt/d/DeepMAL'

# Loop through all files in the input directory and select only the desired columns
for file_name in os.listdir(input_dir):
    # Check if the file is a CSV file
    if file_name.endswith('.pcap'):
        # Load the CSV file into a pandas DataFrame
        print(file_name)
        input_pcap_filepath = os.path.join(input_dir, file_name)

        plugins = [
            NBytesPerPacket(),
        ]

        my_streamer = NFStreamer(source=input_pcap_filepath,
                                        decode_tunnels=True,
                                        bpf_filter="udp or tcp",
                                        promiscuous_mode=True,
                                        snapshot_length=1536,
                                        idle_timeout=9999999999,
                                        active_timeout=9999999999,
                                        accounting_mode=3,
                                        udps=plugins,
                                        n_dissections=20,
                                        statistical_analysis=True,
                                        splt_analysis=0,
                                        n_meters=0,
                                        performance_report=0)
        
        out_file = file_name.split(".")[0]

        my_streamer.to_csv('output-' + out_file + '.csv')
        print(out_file + 'Done...')