from solutions import helpers
import numpy as np
import re

filename = 'input'

[hex_string] = helpers.read_each_line_as_string(filename)

print(hex_string)

binary_string = bin(int(hex_string, 16))[2:].zfill(4*len(hex_string))

print(binary_string)

packet = binary_string


def parse_packet(packet):
    version = packet[0:3]
    version_val = int(version, 2)
    type_id = packet[3:6]
    type_id_val = int(type_id, 2)
    if type_id_val == 4:
        # read_literal_value
        remaining_packet = packet[6:]
        literal_bits = ''
        while True:
            literal_bits += remaining_packet[1:5]
            if remaining_packet[0] == '1':
                remaining_packet = remaining_packet[5:]
            else:
                remaining_packet = remaining_packet[5:]
                break
        literal_value = int(literal_bits, 2)
        return {
            "version": version_val,
            "type_id": type_id_val,
            "literal_value": literal_value,
            "remaining_string": remaining_packet,
            "children": [],
            "packet_length":  len(packet) - len(remaining_packet)
        }
    else:
        # read operator
        length_type_id = packet[6]
        if length_type_id == '0':
            total_length = packet[7:22]
            total_length_val = int(total_length, 2)
            print(total_length_val)
            children = parse_packets_to_length(packet[22:], total_length_val)
            return {
                "version": version_val,
                "type_id": type_id_val,
                "literal_value": None,
                "remaining_string": children[-1]['remaining_string'],
                "children": children,
                "packet_length": 22+total_length_val
            }
        elif length_type_id == '1':
            sub_packets = packet[7:18]
            n_sub_packets = int(sub_packets, 2)
            children = parse_packets_to_count(packet[18:], n_sub_packets)
            return {
                'version': version_val,
                "type_id": type_id_val,
                "literal_value": None,
                "remaining_string": children[-1]['remaining_string'],
                "children": children,
                "packet_length": 22 + sum(pkt['packet_length'] for pkt in children)
            }

def parse_packets_to_length(packet_string, expected_length):
    total_length = 0
    packets = []
    while total_length < expected_length:
        result = parse_packet(packet_string)
        total_length += result['packet_length']
        packet_string = result['remaining_string']
        packets.append(result)

    return packets


def parse_packets_to_count(packet_string, expected_count):
    packets = []
    for ix in range(expected_count):
        result = parse_packet(packet_string)
        packet_string = result['remaining_string']
        packets.append(result)

    return packets


def add_version_numbers(parent):
    total_version_numbers = parent['version']
    for child in parent['children']:
        total_version_numbers += add_version_numbers(child)
    return total_version_numbers


parent = parse_packet(packet)
print(parent)
print(add_version_numbers(parent))