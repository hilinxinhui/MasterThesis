#!/usr/bin/env python3
"""
Check BibTeX file for compliance with GB/T 7714-2015 format.
"""

import re
import sys
from typing import Dict, List, Optional, Tuple

def parse_bibtex(content: str) -> List[Dict[str, str]]:
    """Simple BibTeX parser that returns list of entries."""
    entries = []
    # Remove comments (lines starting with %)
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('%'):
            continue
        cleaned_lines.append(line)
    content = '\n'.join(cleaned_lines)

    # Pattern to match @entry{key, ... }
    entry_pattern = r'@(\w+)\s*\{([^,]+),\s*(.*?)\n\}'
    # Use DOTALL to match across lines
    entries_raw = re.findall(r'@(\w+)\s*\{([^,]+),\s*(.*?)\n\}', content, re.DOTALL)

    for entry_type, key, fields_str in entries_raw:
        entry = {'type': entry_type, 'key': key}
        # Parse fields like field = {value} or field = "value"
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*"([^"]*)"'
        fields = re.findall(field_pattern, fields_str)
        for f in fields:
            if f[0]:  # field = {value}
                field_name = f[0]
                field_value = f[1]
            else:  # field = "value"
                field_name = f[2]
                field_value = f[3]
            entry[field_name.strip()] = field_value.strip()
        entries.append(entry)
    return entries

def check_gbt_compliance(entry: Dict[str, str]) -> List[str]:
    """Check an entry for GB/T 7714-2015 compliance issues."""
    issues = []
    entry_type = entry.get('type', '')
    author = entry.get('author', '')
    title = entry.get('title', '')
    journal = entry.get('journal', '')
    year = entry.get('year', '')
    volume = entry.get('volume', '')
    number = entry.get('number', '')
    pages = entry.get('pages', '')

    # 1. Check author format: GB/T requires surname first, then initials, surname uppercase.
    # In BibTeX, authors are often "Last, First" or "First Last".
    # We'll just check if there are commas in author names.
    if author:
        # Count authors: if more than 3, should be truncated to 3 followed by ", et al."
        authors = [a.strip() for a in author.split(' and ')]
        if len(authors) > 3:
            issues.append(f"作者数量超过3位 ({len(authors)}位)，GB/T要求只列前3位，后加“, et al.”")
        # Check if surnames are uppercase (for foreign authors)
        # This is complex, just note that surname should be uppercase.

    # 2. Check journal title: should be full name, not abbreviation.
    # Common abbreviations that should be expanded.
    abbrev_map = {
        'IEEE Trans. Ind. Inform.': 'IEEE Transactions on Industrial Informatics',
        'IEEE Trans. Veh. Technol.': 'IEEE Transactions on Vehicular Technology',
        'IEEE Trans. Transport. Electrific.': 'IEEE Transactions on Transportation Electrification',
        'IEEE Trans. Power Electron.': 'IEEE Transactions on Power Electronics',
        'IEEE Trans. Intell. Transp. Syst.': 'IEEE Transactions on Intelligent Transportation Systems',
        'IEEE Trans. Neural Netw. Learn. Syst.': 'IEEE Transactions on Neural Networks and Learning Systems',
        'IEEE Trans. Instrum. Meas.': 'IEEE Transactions on Instrumentation and Measurement',
        'IEEE Trans. Reliab.': 'IEEE Transactions on Reliability',
        'IEEE Trans. Ind. Electron.': 'IEEE Transactions on Industrial Electronics',
        'IEEE Trans. Intell. Veh.': 'IEEE Transactions on Intelligent Vehicles',
        'IEEE Trans. Knowl. Data Eng.': 'IEEE Transactions on Knowledge and Data Engineering',
        'IEEE Trans. Pattern Anal. Mach. Intell.': 'IEEE Transactions on Pattern Analysis and Machine Intelligence',
        'IEEE Trans. Cybern.': 'IEEE Transactions on Cybernetics',
        'IEEE Trans. Autom. Control': 'IEEE Transactions on Automatic Control',
        'IEEE Trans. Signal Process.': 'IEEE Transactions on Signal Processing',
        'IEEE Trans. Image Process.': 'IEEE Transactions on Image Processing',
        'IEEE Trans. Med. Imaging': 'IEEE Transactions on Medical Imaging',
        'IEEE Trans. Geosci. Remote Sens.': 'IEEE Transactions on Geoscience and Remote Sensing',
        'IEEE Trans. Comput.': 'IEEE Transactions on Computers',
        'IEEE Trans. Softw. Eng.': 'IEEE Transactions on Software Engineering',
        'IEEE Trans. Parallel Distrib. Syst.': 'IEEE Transactions on Parallel and Distributed Systems',
        'IEEE Trans. Commun.': 'IEEE Transactions on Communications',
        'IEEE Trans. Wirel. Commun.': 'IEEE Transactions on Wireless Communications',
        'IEEE Trans. Inf. Theory': 'IEEE Transactions on Information Theory',
        'IEEE Trans. Netw. Sci. Eng.': 'IEEE Transactions on Network Science and Engineering',
        'IEEE Trans. Serv. Comput.': 'IEEE Transactions on Services Computing',
        'IEEE Trans. Cloud Comput.': 'IEEE Transactions on Cloud Computing',
        'IEEE Trans. Dependable Secure Comput.': 'IEEE Transactions on Dependable and Secure Computing',
        'IEEE Trans. Emerg. Top. Comput.': 'IEEE Transactions on Emerging Topics in Computing',
        'IEEE Trans. Comput. Soc. Syst.': 'IEEE Transactions on Computational Social Systems',
        'IEEE Trans. Games': 'IEEE Transactions on Games',
        'IEEE Trans. Haptics': 'IEEE Transactions on Haptics',
        'IEEE Trans. Affect. Comput.': 'IEEE Transactions on Affective Computing',
        'IEEE Trans. Vis. Comput. Graph.': 'IEEE Transactions on Visualization and Computer Graphics',
        'IEEE Trans. Multimedia': 'IEEE Transactions on Multimedia',
        'IEEE Trans. Broadcast.': 'IEEE Transactions on Broadcasting',
        'IEEE Trans. Consum. Electron.': 'IEEE Transactions on Consumer Electronics',
        'IEEE Trans. Device Mater. Reliab.': 'IEEE Transactions on Device and Materials Reliability',
        'IEEE Trans. Compon. Packag. Manuf. Technol.': 'IEEE Transactions on Components, Packaging and Manufacturing Technology',
        'IEEE Trans. Magn.': 'IEEE Transactions on Magnetics',
        'IEEE Trans. Plasma Sci.': 'IEEE Transactions on Plasma Science',
        'IEEE Trans. Dielectr. Electr. Insul.': 'IEEE Transactions on Dielectrics and Electrical Insulation',
        'IEEE Trans. Appl. Supercond.': 'IEEE Transactions on Applied Superconductivity',
        'IEEE Trans. Nucl. Sci.': 'IEEE Transactions on Nuclear Science',
        'IEEE Trans. Biomed. Eng.': 'IEEE Transactions on Biomedical Engineering',
        'IEEE Trans. Med. Biol. Eng.': 'IEEE Transactions on Medical and Biological Engineering',
        'IEEE Trans. Neural Syst. Rehabil. Eng.': 'IEEE Transactions on Neural Systems and Rehabilitation Engineering',
        'IEEE Trans. Inf. Technol. Biomed.': 'IEEE Transactions on Information Technology in Biomedicine',
        'IEEE Trans. Nanobioscience': 'IEEE Transactions on Nanobioscience',
        'IEEE Trans. Autom. Sci. Eng.': 'IEEE Transactions on Automation Science and Engineering',
        'IEEE Trans. Robot.': 'IEEE Transactions on Robotics',
        'IEEE Trans. Mechatronics': 'IEEE Transactions on Mechatronics',
        'IEEE Trans. Control Syst. Technol.': 'IEEE Transactions on Control Systems Technology',
        'IEEE Trans. Syst. Man Cybern. Syst.': 'IEEE Transactions on Systems, Man, and Cybernetics: Systems',
        'IEEE Trans. Cogn. Dev. Syst.': 'IEEE Transactions on Cognitive and Developmental Systems',
        'IEEE Trans. Evol. Comput.': 'IEEE Transactions on Evolutionary Computation',
        'IEEE Trans. Fuzzy Syst.': 'IEEE Transactions on Fuzzy Systems',
        'IEEE Trans. Knowl. Data Eng.': 'IEEE Transactions on Knowledge and Data Engineering',
        'IEEE Trans. Learn. Technol.': 'IEEE Transactions on Learning Technologies',
        'IEEE Trans. Educ.': 'IEEE Transactions on Education',
        'IEEE Trans. Prof. Commun.': 'IEEE Transactions on Professional Communication',
        'IEEE Trans. Eng. Manag.': 'IEEE Transactions on Engineering Management',
        'IEEE Trans. Technol. Soc.': 'IEEE Transactions on Technology and Society',
        'IEEE Trans. Sustain. Energy': 'IEEE Transactions on Sustainable Energy',
        'IEEE Trans. Smart Grid': 'IEEE Transactions on Smart Grid',
        'IEEE Trans. Power Deliv.': 'IEEE Transactions on Power Delivery',
        'IEEE Trans. Power Syst.': 'IEEE Transactions on Power Systems',
        'IEEE Trans. Energy Convers.': 'IEEE Transactions on Energy Conversion',
        'IEEE Trans. Ind. Appl.': 'IEEE Transactions on Industry Applications',
        'IEEE Trans. Transport. Electrific.': 'IEEE Transactions on Transportation Electrification',
        'IEEE Trans. Veh. Technol.': 'IEEE Transactions on Vehicular Technology',
        'IEEE Trans. Aerosp. Electron. Syst.': 'IEEE Transactions on Aerospace and Electronic Systems',
        'IEEE Trans. Antennas Propag.': 'IEEE Transactions on Antennas and Propagation',
        'IEEE Trans. Microw. Theory Tech.': 'IEEE Transactions on Microwave Theory and Techniques',
        'IEEE Trans. Circuits Syst. I Regul. Pap.': 'IEEE Transactions on Circuits and Systems I: Regular Papers',
        'IEEE Trans. Circuits Syst. II Express Briefs': 'IEEE Transactions on Circuits and Systems II: Express Briefs',
        'IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst.': 'IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems',
        'IEEE Trans. Very Large Scale Integr. VLSI Syst.': 'IEEE Transactions on Very Large Scale Integration (VLSI) Systems',
        'IEEE Trans. Semicond. Manuf.': 'IEEE Transactions on Semiconductor Manufacturing',
        'IEEE Trans. Nanotechnol.': 'IEEE Transactions on Nanotechnology',
        'IEEE Trans. Quantum Eng.': 'IEEE Transactions on Quantum Engineering',
        'IEEE Trans. Artif. Intell.': 'IEEE Transactions on Artificial Intelligence',
        'IEEE Trans. Comput. Imaging': 'IEEE Transactions on Computational Imaging',
        'IEEE Trans. Comput. Biol. Bioinform.': 'IEEE Transactions on Computational Biology and Bioinformatics',
        'IEEE Trans. Inf. Forensics Secur.': 'IEEE Transactions on Information Forensics and Security',
        'IEEE Trans. Big Data': 'IEEE Transactions on Big Data',
        'IEEE Trans. Serv. Sci.': 'IEEE Transactions on Services Science',
        'IEEE Trans. Sustain. Comput.': 'IEEE Transactions on Sustainable Computing',
        'IEEE Trans. Green Commun. Netw.': 'IEEE Transactions on Green Communications and Networking',
        'IEEE Trans. Netw. Serv. Manag.': 'IEEE Transactions on Network and Service Management',
        'IEEE Trans. Mob. Comput.': 'IEEE Transactions on Mobile Computing',
        'IEEE Trans. Cogn. Commun. Netw.': 'IEEE Transactions on Cognitive Communications and Networking',
        'IEEE Trans. Mol. Biol. Multi-Scale Commun.': 'IEEE Transactions on Molecular, Biological and Multi-Scale Communications',
        'IEEE Trans. Broadcast.': 'IEEE Transactions on Broadcasting',
        'IEEE Trans. Consumer Electron.': 'IEEE Transactions on Consumer Electronics',
        'IEEE J. Sel. Areas Commun.': 'IEEE Journal on Selected Areas in Communications',
        'IEEE J. Sel. Top. Quantum Electron.': 'IEEE Journal of Selected Topics in Quantum Electronics',
        'IEEE J. Sel. Top. Signal Process.': 'IEEE Journal of Selected Topics in Signal Processing',
        'IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens.': 'IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing',
        'IEEE J. Biomed. Health Inform.': 'IEEE Journal of Biomedical and Health Informatics',
        'IEEE J. Emerg. Sel. Top. Power Electron.': 'IEEE Journal of Emerging and Selected Topics in Power Electronics',
        'IEEE J. Solid-State Circuits': 'IEEE Journal of Solid-State Circuits',
        'IEEE J. Microelectromech. Syst.': 'IEEE Journal of Microelectromechanical Systems',
        'IEEE J. Photovolt.': 'IEEE Journal of Photovoltaics',
        'IEEE J. Ocean. Eng.': 'IEEE Journal of Oceanic Engineering',
        'IEEE J. Radio Freq. Identif.': 'IEEE Journal of Radio Frequency Identification',
        'IEEE J. Therm.': 'IEEE Journal of Thermal Science and Engineering Applications',
        'IEEE Access': 'IEEE Access',
        'IEEE Rev. Biomed. Eng.': 'IEEE Reviews in Biomedical Engineering',
        'IEEE Signal Process. Mag.': 'IEEE Signal Processing Magazine',
        'IEEE Commun. Mag.': 'IEEE Communications Magazine',
        'IEEE Netw.': 'IEEE Network',
        'IEEE Wirel. Commun.': 'IEEE Wireless Communications',
        'IEEE Trans.': 'IEEE Transactions',
        'IEEE Trans. Ind. Inform.': 'IEEE Transactions on Industrial Informatics',
        'IEEE Trans. Veh. Technol.': 'IEEE Transactions on Vehicular Technology',
        'IEEE Trans. Transport. Electrific.': 'IEEE Transactions on Transportation Electrification',
        'IEEE Trans. Power Electron.': 'IEEE Transactions on Power Electronics',
        'IEEE Trans. Intell. Transp. Syst.': 'IEEE Transactions on Intelligent Transportation Systems',
        'IEEE Trans. Neural Netw. Learn. Syst.': 'IEEE Transactions on Neural Networks and Learning Systems',
        'IEEE Trans. Instrum. Meas.': 'IEEE Transactions on Instrumentation and Measurement',
        'IEEE Trans. Reliab.': 'IEEE Transactions on Reliability',
        'IEEE Trans. Ind. Electron.': 'IEEE Transactions on Industrial Electronics',
        'IEEE Trans. Intell. Veh.': 'IEEE Transactions on Intelligent Vehicles',
        'IEEE Trans. Knowl. Data Eng.': 'IEEE Transactions on Knowledge and Data Engineering',
        'IEEE Trans. Pattern Anal. Mach. Intell.': 'IEEE Transactions on Pattern Analysis and Machine Intelligence',
    }
    if journal:
        for abbrev, full in abbrev_map.items():
            if abbrev in journal:
                issues.append(f"期刊名称使用缩写: “{journal}”，应使用全称: “{full}”")
                break

    # 3. Check year format: should be YYYY, not including month.
    if year and (' ' in year or '-' in year or '.' in year):
        issues.append(f"年份格式可能包含月份或额外信息: “{year}”，GB/T要求只写年份（YYYY）")

    # 4. Check pages format: should be like "9069-9080"
    if pages:
        if not re.match(r'^\d+-\d+$', pages):
            # Check if it's a single page
            if not re.match(r'^\d+$', pages):
                issues.append(f"页码格式可能不规范: “{pages}”，应使用“起止页码”格式，如“9069-9080”")

    # 5. Check for missing volume/number for journal articles
    if entry_type == 'article' or journal:
        if not volume:
            issues.append("期刊文章缺少卷号（volume）")
        if not number:
            issues.append("期刊文章缺少期号（number）")

    # 6. Check for missing title
    if not title:
        issues.append("缺少题名（title）")

    # 7. Check for missing author
    if not author:
        issues.append("缺少作者（author）")

    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_bib_format.py <bibfile>")
        sys.exit(1)

    bib_file = sys.argv[1]
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = parse_bibtex(content)
    print(f"解析到 {len(entries)} 条参考文献条目。")

    total_issues = 0
    for i, entry in enumerate(entries):
        key = entry.get('key', f'条目{i+1}')
        issues = check_gbt_compliance(entry)
        if issues:
            total_issues += len(issues)
            print(f"\n[{key}] 发现 {len(issues)} 个问题:")
            for issue in issues:
                print(f"  - {issue}")

    print(f"\n总计发现 {total_issues} 个格式问题。")
    if total_issues == 0:
        print("所有条目格式基本符合GB/T 7714-2015要求。")
    else:
        print("请注意：上述检查仅基于常见问题，可能未覆盖所有GB/T要求。")
        print("建议使用专业的文献管理软件（如NoteExpress、EndNote）导出GB/T 7714-2015格式。")

if __name__ == '__main__':
    main()