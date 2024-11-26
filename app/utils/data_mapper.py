def get_pcc_step2_data(windows_username, market, is_pcc, is_ds):
    result = {}
    
    if is_pcc:
        result['name'] = f"{windows_username}.pcc@costa.it"
        result['users'] = f"{windows_username}@es.costa.it"
    
    if is_ds:
        groups_map = {
            'DACH': '180, 130, 97, 160, 29',
            'Italy': '100, 160, 29',
            'Spain': '160, 29',
            'France': '110, 160, 29'
        }
    else:
        groups_map = {
            'DACH': '180, 130, 97',
            'Italy': '100',
            'Spain': '160, 29',
            'France': '110'
        }
    
    result['groups'] = groups_map.get(market, 'No specific groups for this market')
    return result

def get_step3_data(market, is_pcc, is_ds, is_tl):
    department = ''
    colas = ''
    skills = ''
    
    if is_ds:
        if market == 'Spain':
            department = "CCH  Com Ops E B2C"
            colas = "E_CBDsManagement; E_CBDsSales; E_CBCostaClub; E_CBShorexB2C; E_Outbound; E_WAB2C; E_CBWOPT; E_CBWB2C;"
            skills = "DsSales:5, DsManagement:4, CostaClub:5, WA_CostaClub, WA_BookingSales, WA_BookingManagement, Spanish, Barcelona"
        elif market == 'DACH':
            department = "CCH  Com Ops DACH B2C"
            colas = "D_WAB2C, CH_D_WAB2C, A_WAB2C, A_CBDsManagement; A_CBDsSales; A_CBCostaClub; A_Outbound;"
            skills = "DsSales:5, DsManagement:4, CostaClub:5, WA_CostaClub, WA_BookingSales, WA_BookingManagement, German, Barcelona"
        elif market == 'France':
            department = "CCH  Com Ops F B2C"
            colas = "F_CBDsManagement; F_CBDsSales; F_CBCostaClub; F_CBShorexB2C; F_Outbound; F_WAB2C; F_CBWOPT; F_CBWB2B;"
            skills = "DsSales:5, DsManagement:4, CostaClub:5, WA_CostaClub, WA_BookingSales, WA_BookingManagement, French, Barcelona"
    
    elif is_pcc or is_tl:
        if market == 'DACH':
            department = "CCH Com Ops  DACH PCC"
            colas = "A_PCC; A_PCCDefault; A_CBWB2CPCC; A_CBWOPTPCC; A_CBFQPCC; A_CBFQPCCDefault; A_Outbound;"
            skills = "A_PCC:5, D_PCC:5, CH_D_PCC:5, DsSales:1, DsManagement:1, German"
        elif market == 'France':
            department = "CCH  Com Ops  F PCC"
            colas = "F_PCC; F_PCCDefault; F_CBWB2CPCC; F_CBWOPTPCC; F_CBFQPCC; F_CBFQPCCDefault; F_Outbound;"
            skills = "F_PCC, DsSales:1, DsManagement:1, Barcelona, French"
        elif market == 'Spain':
            department = "CCH  Com Ops E PCC"
            colas = "E_PCC; E_PCCDefault; E_Outbound; E_DsManagement; E_CBDsManagement; E_DsSales; E_CBDsSales;"
            skills = "E_PCC:5, DsSales:1, DsManagement:1, Spanish"
        elif market == 'Italy':
            department = "CCH CC ITA PCC"
            colas = "I_PCC; I_PCC_Default; I_CBWB2CPCC; I_CBWOPTPCC; I_CBFQPCC; I_CBFQPCCDefault; I_Outbound;"
            skills = "I_PCC, Barcelona, Italian"
    
    else:
        if market == 'DACH':
            department = "CCH  Com Ops  DACH B2C"
            colas = "A_DsManagement; A_CBDsManagement; A_DsSales; A_CBDsSales; A_CostaClub; A_CBCostaClub;"
            skills = "DsSales:5, DsManagement:4, CostaClub:5, German"
        elif market == 'France':
            department = "CCH  Com Ops  F B2C"
            colas = "F_DsManagement; F_CBDsManagement; F_DsSales; F_CBDsSales; F_CostaClub; F_CBCostaClub;"
            skills = "DsSales:5, DsManagement:4, CostaClub:5, French"
        elif market == 'Spain':
            department = "CCH  Com Ops  E B2C"
            colas = "E_DsManagement; E_CBDsManagement; E_DsSales; E_CBDsSales; E_CostaClub; E_CBCostaClub;"
            skills = "DsSales:5, DsManagement:4, CostaClub:5, Spanish"
    
    return {
        'division': 'UECC',
        'department': department,
        'colas': colas,
        'skills': skills
    }