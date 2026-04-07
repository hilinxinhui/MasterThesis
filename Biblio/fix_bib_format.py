#!/usr/bin/env python3
"""
Fix BibTeX file for compliance with GB/T 7714-2015 format.
Automatically fixes: author count, year format, page format, journal abbreviations.
Outputs a new file and a report of issues that require manual attention.
"""

import re
import sys
from typing import Dict, List, Optional, Tuple, Set

# Expanded journal abbreviation to full name mapping
JOURNAL_ABBREV_MAP = {
    # IEEE Transactions (common in the file)
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
    'IEEE Trans. Consumer Electron.': 'IEEE Transactions on Consumer Electronics',
    # IEEE Journals
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
    # Common journal abbreviations
    'Nature Commun.': 'Nature Communications',
    'Nature Energy': 'Nature Energy',
    'Nature': 'Nature',
    'Appl. Energy': 'Applied Energy',
    'J. Power Sources': 'Journal of Power Sources',
    'J. Energy Storage': 'Journal of Energy Storage',
    'Renew. Sustain. Energy Rev.': 'Renewable and Sustainable Energy Reviews',
    'Reliab. Eng. Syst. Saf.': 'Reliability Engineering & System Safety',
    'Mech. Syst. Signal Process.': 'Mechanical Systems and Signal Processing',
    'Inf. Fusion': 'Information Fusion',
    'Eur. J. Oper. Res.': 'European Journal of Operational Research',
    'Chem. Eng. J.': 'Chemical Engineering Journal',
    'Electrochim. Acta': 'Electrochimica Acta',
    'Meas.': 'Measurement',
    'J. Electrochem. Soc.': 'Journal of The Electrochemical Society',
    'Energy Environ. Sci.': 'Energy & Environmental Science',
    'J. Franklin Inst.': 'Journal of the Franklin Institute',
    'Sensors': 'Sensors',
    'Ocean Eng.': 'Ocean Engineering',
    'Knowl.-Based Syst.': 'Knowledge-Based Systems',
    'Friction': 'Friction',
    'J. Sound Vib.': 'Journal of Sound and Vibration',
    'IEEE/ASME Trans. Mechatronics': 'IEEE/ASME Transactions on Mechatronics',
    'IEEE-CAA J. Autom. Sin.': 'IEEE-CAA Journal of Automatica Sinica',
    'J. Manuf. Syst.': 'Journal of Manufacturing Systems',
    'J. Energy Chem.': 'Journal of Energy Chemistry',
    'Energy Storage Mater.': 'Energy Storage Materials',
    'eTransportation': 'eTransportation',
}

def parse_bibtex(content: str) -> List[Dict[str, str]]:
    """Parse BibTeX content into a list of entries with positions."""
    entries = []
    # We need to preserve the exact format, so we'll find each entry's start and end
    # Pattern: @type{key, ... } with possible newlines inside
    # Use DOTALL to match across lines
    pattern = r'(@(\w+)\s*\{([^,]+),\s*(.*?)\n\})'
    matches = list(re.finditer(pattern, content, re.DOTALL))

    for i, match in enumerate(matches):
        full_match = match.group(0)
        entry_type = match.group(2)
        key = match.group(3)
        fields_str = match.group(4)

        # Get start and end positions
        start = match.start()
        end = match.end()

        # Parse fields
        entry = {
            'type': entry_type,
            'key': key,
            'start': start,
            'end': end,
            'original': full_match,
            'fields': {}
        }

        # Field pattern: field = {value} or field = "value"
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*"([^"]*)"'
        field_matches = re.findall(field_pattern, fields_str)

        for fm in field_matches:
            if fm[0]:  # field = {value}
                field_name = fm[0].strip()
                field_value = fm[1].strip()
            else:  # field = "value"
                field_name = fm[2].strip()
                field_value = fm[3].strip()
            entry['fields'][field_name] = field_value

        entries.append(entry)

    return entries

def fix_author(author: str) -> Tuple[str, List[str]]:
    """Fix author field: limit to 3 authors, add ', et al.' if needed."""
    if not author:
        return author, []

    issues = []
    # Split by ' and ' (BibTeX standard)
    authors = [a.strip() for a in author.split(' and ') if a.strip()]

    if len(authors) > 3:
        issues.append(f"作者数量从 {len(authors)} 位减少到 3 位")
        # Keep first 3 authors
        fixed_authors = authors[:3]
        # Add ', et al.' to the last author
        fixed_author = ' and '.join(fixed_authors) + ' and et al.'
        return fixed_author, issues

    return author, issues

def fix_year(year: str) -> Tuple[str, List[str]]:
    """Fix year field: extract only 4-digit year."""
    if not year:
        return year, []

    issues = []
    # Try to find 4-digit year
    year_match = re.search(r'\b(19|20)\d{2}\b', year)
    if year_match:
        extracted_year = year_match.group(0)
        if extracted_year != year:
            issues.append(f"年份从 '{year}' 清理为 '{extracted_year}'")
        return extracted_year, issues
    else:
        issues.append(f"无法从 '{year}' 中提取有效年份")
        return year, issues

def fix_pages(pages: str) -> Tuple[str, List[str]]:
    """Fix pages field: normalize dash to single hyphen."""
    if not pages:
        return pages, []

    issues = []
    # Replace various dash characters with single hyphen
    # Unicode dashes: – (en-dash), — (em-dash), ― (horizontal bar)
    normalized = pages.replace('--', '-').replace('–', '-').replace('—', '-').replace('―', '-')
    # Remove spaces around dash
    normalized = re.sub(r'\s*-\s*', '-', normalized)

    if normalized != pages:
        issues.append(f"页码从 '{pages}' 规范化到 '{normalized}'")

    return normalized, issues

def fix_journal(journal: str) -> Tuple[str, List[str]]:
    """Fix journal field: expand abbreviations to full names."""
    if not journal:
        return journal, []

    issues = []
    fixed_journal = journal

    # Check for abbreviations in the map
    for abbrev, full in JOURNAL_ABBREV_MAP.items():
        # Handle abbreviations with or without braces
        pattern1 = r'\b' + re.escape(abbrev) + r'\b'
        pattern2 = r'\{' + re.escape(abbrev) + r'\}'

        if re.search(pattern1, fixed_journal) or re.search(pattern2, fixed_journal):
            # Replace abbreviation (with or without braces)
            fixed_journal = re.sub(pattern1, full, fixed_journal)
            fixed_journal = re.sub(pattern2, '{' + full + '}', fixed_journal)
            issues.append(f"期刊名称从 '{abbrev}' 展开为 '{full}'")
            break

    return fixed_journal, issues

def check_missing_fields(fields: Dict[str, str]) -> List[str]:
    """Check for missing fields that require manual attention."""
    issues = []
    entry_type = fields.get('type', '')

    # Check for journal articles
    if 'journal' in fields or entry_type == 'article':
        if 'volume' not in fields:
            issues.append("缺少卷号（volume）")
        if 'number' not in fields:
            issues.append("缺少期号（number）")

    return issues

def fix_bibtex_entry(entry: Dict[str, str]) -> Tuple[Dict[str, str], List[str]]:
    """Fix a single BibTeX entry."""
    fixed_fields = entry['fields'].copy()
    all_issues = []

    # Fix author
    if 'author' in fixed_fields:
        fixed_author, issues = fix_author(fixed_fields['author'])
        fixed_fields['author'] = fixed_author
        all_issues.extend(issues)

    # Fix year
    if 'year' in fixed_fields:
        fixed_year, issues = fix_year(fixed_fields['year'])
        fixed_fields['year'] = fixed_year
        all_issues.extend(issues)

    # Fix pages
    if 'pages' in fixed_fields:
        fixed_pages, issues = fix_pages(fixed_fields['pages'])
        fixed_fields['pages'] = fixed_pages
        all_issues.extend(issues)

    # Fix journal
    if 'journal' in fixed_fields:
        fixed_journal, issues = fix_journal(fixed_fields['journal'])
        fixed_fields['journal'] = fixed_journal
        all_issues.extend(issues)

    # Check for missing fields (manual fixes needed)
    missing_issues = check_missing_fields(fixed_fields)
    if missing_issues:
        all_issues.append("需要手动补全: " + ", ".join(missing_issues))

    # Reconstruct the entry
    fixed_entry = entry.copy()
    fixed_entry['fields'] = fixed_fields

    return fixed_entry, all_issues

def reconstruct_entry(entry: Dict[str, str]) -> str:
    """Reconstruct BibTeX entry from parsed data."""
    fields = entry['fields']
    lines = []
    lines.append(f"@{entry['type']}{{{entry['key']},")

    for field_name, field_value in fields.items():
        # Use braces for field values
        lines.append(f"  {field_name} = {{{field_value}}},")

    # Remove trailing comma from last line
    if lines:
        lines[-1] = lines[-1].rstrip(',')

    lines.append("}")
    return '\n'.join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_bib_format.py <bibfile> [output_file]")
        print("  If output_file not specified, uses <bibfile>_fixed.bib")
        sys.exit(1)

    bib_file = sys.argv[1]
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        output_file = bib_file.replace('.bib', '_fixed.bib')

    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"正在处理文件: {bib_file}")
    print(f"输出文件: {output_file}")

    # Parse entries
    entries = parse_bibtex(content)
    print(f"找到 {len(entries)} 个参考文献条目")

    # Process each entry
    fixed_entries = []
    all_reports = []

    for i, entry in enumerate(entries):
        fixed_entry, issues = fix_bibtex_entry(entry)
        fixed_entries.append(fixed_entry)

        if issues:
            report = f"[{entry['key']}] 修改: " + "; ".join(issues)
            all_reports.append(report)

    # Reconstruct the entire file
    # We need to replace each original entry with the fixed one
    # Build the new content by replacing parts
    new_content_parts = []
    last_pos = 0

    # Sort entries by start position
    sorted_entries = sorted(entries, key=lambda x: x['start'])
    sorted_fixed = sorted(fixed_entries, key=lambda x: x['start'])

    for orig_entry, fixed_entry in zip(sorted_entries, sorted_fixed):
        # Add content before this entry
        new_content_parts.append(content[last_pos:orig_entry['start']])
        # Add the fixed entry
        new_content_parts.append(reconstruct_entry(fixed_entry))
        last_pos = orig_entry['end']

    # Add remaining content after last entry
    new_content_parts.append(content[last_pos:])
    new_content = ''.join(new_content_parts)

    # Write fixed file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Write report
    report_file = output_file.replace('.bib', '_report.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"参考文献格式自动修正报告\n")
        f.write(f"原始文件: {bib_file}\n")
        f.write(f"修正文件: {output_file}\n")
        f.write(f"生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

        if all_reports:
            f.write(f"共修正 {len(all_reports)} 个条目的格式问题:\n\n")
            for report in all_reports:
                f.write(report + "\n")
        else:
            f.write("未发现需要自动修正的问题。\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("注意：以下问题需要手动处理（无法自动修复）：\n")
        f.write("1. 缺少卷号（volume）或期号（number）的条目\n")
        f.write("2. 作者姓名格式（GB/T要求姓大写，名缩写）\n")
        f.write("3. 电子资源访问日期和URL格式\n")
        f.write("4. 其他特殊文献类型（标准、专利等）的特定格式\n")
        f.write("\n建议：使用文献管理软件（NoteExpress/EndNote/Zotero）导出GB/T 7714-2015格式。\n")

    print(f"修正完成！已保存到: {output_file}")
    print(f"详细报告: {report_file}")

    if all_reports:
        print(f"\n修正摘要（共 {len(all_reports)} 处修改）:")
        for i, report in enumerate(all_reports[:10]):  # Show first 10
            print(f"  {i+1}. {report}")
        if len(all_reports) > 10:
            print(f"  ... 以及 {len(all_reports) - 10} 处其他修改")
    else:
        print("未发现需要自动修正的问题。")

if __name__ == '__main__':
    main()