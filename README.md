# A Quantum Code Research Project

This project builds upon my 2024 summer research with Professor Noah Aydin at Kenyon College, focused on discovering and optimizing classical and quantum error-correcting codes.  
The paper associated with this work is available here:  
http://dx.doi.org/10.48550/arXiv.2410.12167

## Project Objectives

1. **Optimize Quantum Code Searches**
   - Run Magma programs for large-scale code searches using automated Python scripts.
   - Compare results with existing entries in the online quantum code library.
   - Review recent literature and implement promising methods for quantum code construction.

2. **Update the Quantum Code Library**
   - Resolve database issues such as duplicates and outdated entries using C# programs.
   - Use Python (with BeautifulSoup) to scrape and add newly published quantum codes from online sources.

The online quantum code library is available at:  
http://quantumcodes.info/

## Software System Architecture

Each folder in this GitHub repository corresponds to a specific paper we reviewed. For each paper, I implemented the theorems using Magma, and in many cases, conducted a mass search for new codes.

### 1. Supercomputer Server
After accessing the supercomputer server, Magma scripts can be executed with the following command: magma < input.txt > output.txt
- Input: Code size (n) and field size (q)  
- Output: A list of quantum codes generated using CSS or Hermitian constructions.  
Some output files are trimmed to save space but full results are stored on the server.

### 2. Online Quantum Code Library
- Hosted on a web server (discountasp.net) and paid yearly by Professor Aydin.
- The database is managed using SQL and C# tools for data cleaning and insertion of new entry using VSCode.
- Web scraping is performed using Python scripts using VSCode.
