#!/bin/bash



# Loop through all SVG files in the current directory

for svg_file in *.svg; do

    # Check if there are any SVG files

    if [[ -e "$svg_file" ]]; then

        # Define the output PDF filename

        pdf_file="${svg_file%.svg}.pdf"

        # Convert SVG to PDF using Inkscape

        inkscape "$svg_file" --export-filename="$pdf_file"

        echo "Converted $svg_file to $pdf_file"

    else

        echo "No SVG files found."

    fi

done

