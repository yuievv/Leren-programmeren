from test_lib import test, report
import math

def afronden_naar_vijf_centen(bedrag: float) -> float:
    bedrag_in_vijf_centen = bedrag * 20
    
    afgerond = round(bedrag_in_vijf_centen)
    
    return afgerond / 20

def test_afronden_naar_vijf_centen():
    test('afronden_naar_vijf_centen', 62.60, afronden_naar_vijf_centen(62.60))
    test('afronden_naar_vijf_centen', 76.60, afronden_naar_vijf_centen(76.61))
    test('afronden_naar_vijf_centen', 28.80, afronden_naar_vijf_centen(28.82))
    test('afronden_naar_vijf_centen', 2.25, afronden_naar_vijf_centen(2.23))
    test('afronden_naar_vijf_centen', 28.35, afronden_naar_vijf_centen(28.34))
    test('afronden_naar_vijf_centen', -42.85, afronden_naar_vijf_centen(-42.85))
    test('afronden_naar_vijf_centen', 31.05, afronden_naar_vijf_centen(31.06))
    test('afronden_naar_vijf_centen', -138.45, afronden_naar_vijf_centen(-138.47))
    test('afronden_naar_vijf_centen', 14.90, afronden_naar_vijf_centen(14.88))
    test('afronden_naar_vijf_centen', 149.70, afronden_naar_vijf_centen(149.69))

test_afronden_naar_vijf_centen()
report()