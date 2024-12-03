"""
Everybody Codes 2024
Quest 1, Part 3
"""

DEBUG_MODE = False
CLUSTER_SIZE = 3

demo_input_str = (
    "xBxAAABCDxCC"
)

input_str = (
    "BDxDADxCBDxDBxBCCxDxDxACxCADCDDxDDxDCDBABDDCCAxxxBADAxBCBDBBDDCxDCCADADAA"
    "xxxDADBxCxDxxDxCBDADDDACBxxDxBBAxAAxDxBCDxBxDBCxBCBDxCxCDDABAABDxBBAxCAAB"
    "BCCCDDxACBAxxCxBDABBCBBAAxDCDCAAxCxDBBCBCxxBDxABBAADxADACDDDABACABBxDCCxB"
    "xCDCxDADxBxDDCCDxCDDDxBxAxDDCBBCCDxxxDADDAxxACxCxACxBxCAAADxBDAADDDCABBBC"
    "BDxADCDDBDDADBxABCBDAADxDxxDAxAxBDxCxxCBAxBCADxBxDCxBDACxBDACADxABxCDCBBC"
    "CCDxAxDDBCxBBDBCBCxCCCAAAAxBCBBBACDxABxBBBBxDAxxxDDBBCCDxACCAAxCxxACBBDBA"
    "ACBBDCCDBCxBBCABBBDABDxCBxDxABAxBACCBxxDDDDBDxDxCBCCAACxBCBADDCDCxxDACxDx"
    "ABxADACDCBBBDDxCDAxACDDBACxABDxBDDxDCBDxxDDDBxADCCADBCCADCDxDBADCABAxxAxA"
    "AAxBBCCxABDDCACACxxDxBABDACACCDDAADDxBxCDxDAxDxBxDACACDxCCBBBBxAxxxDxxxxA"
    "AAxBBCBADCDCxCAADxDxxDxCAAxACADAxDDBDDDDxAxAxCxxBxBxDDACDCxxAxDDDABAxDxCx"
    "BBBBBADDAACDDABCxxDDCCxDBADCAAxBACAABDCBBxAABAAxCACxCxADDCCDBBCCAxBDBBDBB"
    "BDAABDAxxDCCxxxBxDxBCDBBBCDxABBBACCDAxxxDDxCCBBCAABCBCDDxAxAxCxDDBxCAACAx"
    "BDAxACxBxBADDBCDDAACCADACxxCAxxACDxBxABxACxBACADBBCBBDBxDDDxxAxDBACxxxxxD"
    "CDAxBBxBCBADABDBABxxDDBBADDxACBCABDBBDBCDxBxCxxDCBDxDCBCBBxxABCDBAxBCDCCA"
    "xBDCDBCDCxxBDxCBAxADCxACxCCDACCBxBCBBAACBDCCDxxDBDABBCxAxCBxCCCxAxCDAxDCD"
    "CBABxDCxDDCAxCACDCxABDCCCACxDxDACBDCxADBBBBDACBBDBxxBxxBDxxCxBDCxDDCBCACB"
    "DAxBxCCxDBDCBCxBDAxBCDDDCBCAABBCCCCBAADAxBADCDCDADBACBBDBABACxxxCCCADABCC"
    "xxABxBBDCxCABBBAAACxBDDxxACBBBBxCDCxCCCBDABCDCxDCxACCABBDDDxxABAxCCAACBAC"
    "BBBBCxCDCCBxCBDCAAxxAxBxACDxCxDBDxDADACCDAAAxDADAxACBBDBACABDxCxCAAABDAxx"
    "AxxBDBDCxxDAxBxADxCCxAADBDxxAxCCDDCDAxDDxBxBDBDDDDxBCxxCBABDxDABDxDxABDxx"
    "CBBADCDCCCDACDBBADBCABBCxACACCxBDBDACxxABADBxDCABxACxDxADDBBDxDBxxxDxBxAB"
    "DDBAABDDDACxxADCBxADBBCxCxBxCxACxDDDxxCCCxCBCBACCxxxCADBBACDAACDACACABDBD"
    "xCBDxACxBBxxCABDAxCDxxDDACDBADCABxAxDCCBDBAAxxACxDBDBCBACBCxABxABBCBAACBD"
    "ACDBCBACACBACDDADCCxxDCCxDDAxxxxxBBDAAxDxCAxDCDCBCxCAxCDAACxACxCBxACCBxBB"
    "CBBDxCxDxDDDBBDDBDBADDDxDDBACxCxBBABCADADBDCxBAxCBDACxCBDxDBDBCACADBCABxD"
    "BCACxAAxxCBCxBBCCxCBADADABDxBDDAxDCADxBxBBDAAxCBBDCBBCCDABBAxCCCBDCABCDxA"
    "xBxxDxDxDBCAxCBAxCCABDAAxxADAxxAxCABxxAxBCCDCABBAxABAACABBCBCACAAACCABxxA"
    "BBBDCAxABAAAAxxDBDDACDCxxCxxCxABxDABBDAxADBACxDCBxAAADxCACDACxCCxDBDDxxBA"
    "xDxBDDDxCBxDxDCCBxDDABCACxCCADAxABxxAAADBADDCBDAxBDCDxxxxDDDBCBxDBAxABDBB"
    "xACCxAACCBBxBBBxDCDAAxxACDBADxDCBDxBDCCDBBACxBxDACBDxAAxCxCxxCBABDCxCxBDA"
    "BDBCBDBCADACACABDCBADxCCBACDADADAABCBCDAACDCxDDCBBCxCDBCDABDDxAADCABCBCBA"
    "BACADBABBABBCAxCCxBBCCxBDCBBABDxxxBADDCAABxBBDDCBBxDAxDACBBDCDBDBBxxDCBCA"
    "xxDxBDACDxxAABAADDxBCACDCDBCADxBCCAABDAADDADxDxADBxDDAxBDCBBAADDBBxABCDCx"
    "DAACBDBDxCCACxBBCBBBBCCBxDAxDCBBCCxCCBAABACCCBxCADCxxCDBDACDDACxBxxDxADAB"
    "xDAxBAxBBDAxBDACxDBCxxBxxDAAAABxxADCCBCCBADDCBABCBDDDCCDBxxxxDCBCCABBBxCA"
    "BCxDxCCDCDCDDBBACCBBDADBxDxAxxxADAxxBADxAACxxxAxADACAxAxCDCCCxxxACxxBCxAx"
    "xxABDBDxABDxxDDCAACCAAxxACBCCxADxCDxCDxxxADCBxCDBCDCxxDDDxCxBABCBxxBADCBx"
    "DxCCBBBDDACxDCBBBDBCxDDACDBADxABxBACAxxDBBACCxCCAADDBACBCDDxABBxxBBCBDBAx"
    "BDDxDCxDBDCABxACxDBxxDDBADDBAAAABCxCACADDxACDBxxxxDDCBxDCBBABBxABBCCCCAAx"
    "xABxxxDCDBCxAxADDDCABxCBCCAxDBABDBABABxBCxBBxCBDCDDADDBBAABDDBABAADBDxADD"
    "DAADxAABxBBBBCxDABABCAABxBADDBDBDBDBBDDBCCBABADAxABCDABCBCBBxDAADBAAxCADA"
    "CABDxxBDCDAABADCDDxxBCCBxDCBACDDBBABBDBDBCDDCDCxxACABCDxADDCxCAABDBADxAAC"
    "xCCAxBBxBBDAxDCCAAxxCBADBxBDxDDBBCxxxxABAACxADCDCBxxDADAxxDxBAxBDDBxDCCAD"
    "xBDBCxxDDxBADxCBBxCCBAxxDBxACBDCBBxCBBCCCBxAxBAAxDCxBxxDBDxxCBxADxBAAABAx"
    "DBDCxBxDBABBDBDACBABACBAxxCCCCDBCCABDBxCCxADxBBBBAAxxBACBBBAxCCCxxxBBAxxC"
    "AxACBACADAACBxAACAxBADCAACBADCBCxBxxBBCBBBABBCxBBxxDBCDBDABBxxABCxBCCCAxC"
    "CCBCxAxACDxADxDACxADxBxCBDBCDACABxAxxBDDAABDABCDAxDDDxBCABDxCCBDADDDABxDC"
    "xABxxBCxCABxxABxBAABAxDxBACCDxxxBADDACCDDCADBCBxAACCADBxDDxCBCxABBCCxAxAD"
    "ACxACBDCDBDCADAxABBBADCCBxDABDDBxADDAAxxCxDCBBBAACCBDBABCDCCCABCxADxCxxBD"
    "xDABBAxBxBxDxAABCDxxAADBCBBBAxBxABDBxxBDDCCACBADxxBAxBACxCBBCDACAxDBDBBBC"
    "CACAxABCCACBCCABBxACDADACBDBCCADCxxBBBCDADAAxBxBDxBAxCBBCCBBDxCBCCCDDDDxC"
    "BBAxBBDCCxBDDBCxCBxxCBxACCBxDBDAxBCABDCDBCxCCxDBxDxBAAAxxAxADDxABCDDDAABx"
    "xCCCCxDADDACxDDBCCBDBDCxDCBxADxCCxxAAACCCADACDDCABBCDBDBACxxxCDxxxBxBCxAB"
    "BBxBBADADAxCBCCDCDBDDCCBABCACxCDBDDCBDDBDDDDCxADBADDxABADCBxCBxCACCDCCBDx"
    "BBCCAADBDCBBCDBDCDCCxDCBCDDBCBxBBABxxACBABxDDDCBBCCBCCACDDxxDCCDAABDCCxDA"
    "BACxCxxxDDxxDADBDBAxCCCCABAACxxAxBACDxxCBxxACxBDBBCCDDCDCDDDDAxCDBADAxAxC"
    "CDBDDCAAADDCCBBCDDBDADxDADxBADxCADCABACDAACxBACDxCDBBCABxDxBxxCDDBxACBADB"
    "DxCAxDDBCACBCCCDxBDxBDxCDABBABCDCCDBDDBABDxxBACCxBDxCDDBDAAAxxxDCxACCDCBC"
    "DDBBxCBxBACCxACxAxACCCxCCAxxAAxxCDBBDDCADDDDxCCADCAADCDDxDDCBCAACCCABCCCD"
    "xxxxxABDCxBxBxDDDxCxCDDxBACBADCDDAADBBCBBCAAACDxCDBDBADCCDABCABDCxACBBBCx"
    "DBBBxCBxxCCABACBDDCDAABDxBxxABBABCCxBxDDBCxAAxBABCBDCDABABxAxDBADBDBDCACD"
    "CxBCBDCDCAACDAxDAxACBxBCABDBBCCxBDBDBAxxCBCDBAAABDBxxxCBDxCBBDCCDDBxBCxCC"
    "ACxABBCCBCBDBxDxCxDDxCDBxxCDDABDBxxDCDACCxBABDCDCDBCCACxBxACDAACxBxBxCDAA"
    "xDCCBABADAADBxABDDCDCCBDBCCxADBCADBDDACBAxCxBDBAAxBCCAAxDCABCCCxDAAAxBCDA"
    "CABBCBACxACAxBDCDDDCBBCBDABDCDxBDxACBDABACACxBAxxCxDBxCBBACCAxxCxCDxBABxC"
    "AxACADxBBDCCxxxxDCxADBAADACAxDCBxCCDCxBCxBDBBCABCAABCBACAAACxBDxAACCDCCxx"
    "xADBAxDxxABACCxDABBCBxCACBBBACBBBxxABBAxBDCABDxxACDCACCxADBADxACAxCxxAxCC"
    "ABxxxCBAACDAAADAADCAxBDDBDxDBDAxBABACBCBBBCCxDBBACxDCxxxxBCACAACCADDBBCCB"
    "BABAADBACABBAxCxAACxCDCAAxCBCDCBBBCADxxxBxCACCBxxAxDCCBDAAABDAABCBDDDCBBC"
    "BCCDxCABBDxDDBDDBADBCBBBBADxDDCCBACBCAAxAxDCCADDCDBxBCAxADBxBBCxCCCABBBCC"
    "DAABBxAACBBCAxCxABCCACCxBCCBCxCDADCBDAxxCxCBBCBDBxBxAAxBCCxCxDxAxBxDCCDAA"
    "CABxABCCABxDxxCBxADCAxDADCBBDBBCCBBCDDxDDAxCCDADCBDBBBxDDDCDxDDxAABBDBCCC"
    "BBBDBxDDCDDxABBBADACCDCAxDDDCDBDxACCxDxCxCCCCCCxCBBADACxxBBxACADBAAAxABDx"
    "CABDADCxCxAxDCDBxCCCCCBBBBAxADxDBDABABACACCAADBDABxCxABCxxAAAxDDCBADDABCD"
    "xBBBDBAABDBACxBCDDBDCBABBBBDBBCDAxABCCCAxCAxADBBxDBCxCxBCABCDDCACxDCxBCxB"
    "CxCBDCBBCxDBACAxDBBBxCBACxBxDABADBBBxCxxCxBCBxABCDCDxCDCAxDCABBBxxDBDBADx"
    "ADxxDADBCCDDxCBCxxBxDxBCBxACADCBAxACADCAACCCxxBDDDxDAABBBxBCDDAACBDxxDCxD"
    "CAxxACBCAxAACDxCCABDCxCDAAxxAADxABBCDBxADCxBxDxxDBAAxxDxAACxCxABBBCBADDDx"
    "DCDACCBBDCxACBDBCBCCCCxAxABDDDCCDBxxCBCxAABDDDACxDDAxxCDACCDCDDxDxABBDDCx"
    "xxBADCBxCCBDDDDDABCCAAxABBCBxADDDBDxBCABDxxDAAABCABCCCBAACAAABDADDABABDxB"
    "DABCADDxBCxABDCDxBADADxBCDADABCxxCADDDBBxBBxADxxDDxABCxBABBABDBCxxADxDxCC"
    "DDDCAxxADxDxDCCBADBDCCBxDBABDxDBADxADCxBxAxBxxBxCCCDADAAAAABABCDDBCBCDBAA"
    "BxCABAxAABDABDADAxCCCxCCxCxAxxBxxxxBBAACACCACBAxDBDxDBAxBAACABDADCACDCxxB"
    "CBxCxDCDDCCBxCBAxCCCDDADBAxxDBxAxCCCCBDDDAxCxBDDxxADCxBxBCAxCADAAxCCDBxAB"
    "DDDxBDBDBxDCAAACCBABAxAAxDCDCxDxxxBCCBDDABDCBxDDDxCxACDxxBDCACBCCAADCDBCB"
    "AAABCxDAxDBBBDxCABxDBACBBAACADACxBxDCBBCxDAAxBxAABxAxBxCACxDDxDDCBAABABxx"
    "ABACBCDABDCCAxDxBDxBxxABBBBCDCBBDDDxBxDCCDCDDDDBBxDDBCAAABCAxDxACDBDBxxCx"
    "DBBAxxCBBBBCCCACxBxDABCCBBDDAACxxDxBBBACACBDxDCBDxCDCDxABDxDACxDBCBBBDAAx"
    "BxCAADBABxADBDDCDBADBxDDACCCBxCCDAADxDxADABABBxxBCACCCACBCADCAxCBxCBxxCDB"
    "BDDACDBCCCxAACDBxCCxBDADAADDCADxADxDBDxxBAxxCCxCBAACCACxBADADACBBDCAAAxBB"
    "ADCDxCCCBAABABxCAxACBAxxBBCxDBBDCxAACDDBxCCAACBABACACCxDxBxBCDDBxABCCAxxD"
    "CxxBBDAxBCBxCCDBCxxxCxxACxDABxBxCCBBDBxBDAAACxBDDBxCxxAxBxADDxCBDACADBxAC"
    "xDBDAxAxCBxADxBDBCDBDACACBCCCxAADBxBAxCxBDxCBDAABDBCBxDxxDDCAxDBACADBDDxB"
    "xBCDACxxADACxCxAxDxBxAxxBxBBACxDCDACDBBABBDCBCDCDBBDDBBBBAAxDDDBCCDDxCACA"
    "CBCBBCCCDDCBCDBBxxxCCCADCCDAxCABBAxBABCxxBACBDAxxAxCCBDAABACDCBxDAxBACDCx"
    "BAABDxCDxBxACCDCCAADDABxADBxBCxxBCDBCABxBAAxDDCAxxAACCAxCACDDxBDDAABBACBB"
    "CAxCxBBBABCBBBBBCxCCABDDxDCDBDDDCDBDxxCCCDADBDxBxBDDCBCAABDCxAxxDBBDBACxB"
    "BACDDDDBBBBAxBxDCADDACBCBDAxBCCxABCDBCAxABBDxxCCCBCDxCDDxBBBAxxADDAACDCBC"
    "xBDADAAAxxBCBACDADxAABDDxCDxxxCxBADAxDCBCBBxAACCDxBBCBDAxACDDxxDxAxDACBxx"
    "DDxDCxCABBxCCDCxADCxCxxADxDBCDCBCBACBADDDCCCBxxBBBBDDACDCxBDBDAxCDDxAxCxC"
    "BBCDCCBxCDDxACxxAACxCCDxBBABBBxxBADAAACBxxDBBDBxxCCxDxBABDACAxxCDCDAxxDAD"
    "BADBxADCDBDDBACxxABAADBDADCDCDAABCCxBDCABDDCxDCxDCCDDBxxDDDABBBCDBDDxDCAA"
    "DDBCCDBCAAAAABBCBADCABABDDBDxCCDDCCxDCCABCCDCBAxDCxxxABACAxCBDCxBDBDxDBAA"
    "xDxDDxADxxxxBAxxBADCCADDDCCxADBCCxxxAxACDDxBCACBCDAAxDBxBCBDBxBBBABAAxxDx"
    "xDAADCxCDBxADDCxDDxDCCxDCCBDCAxxCxCDDADCxDxCxDxAAxBxAAxCBxBCDCxDBBCDBDABx"
    "BCDxxxDxCCxCCBCDBBCDBxDCDCxxxDACCCDBACxCxBCBAAxAABADABxDBBAAABBBADCBDxAAB"
    "ACxBCxDxBBxxCCAxBCDDBxAAACBBBABBCxxAxCACAxxCCxDADDABBxAxACBACDDCBDxxDxDAA"
    "ABBDDAADxDxDxxDCDBCCADBCCBBAACADBDCABBADADAAxAxACxBBADDDxCAxxBBDCxCBxDBxC"
    "ACAADAxCCDABAxDCBDCCBDACxxBDDACCxAAADCCDAABDCABDDxACCAxDBCBxxCxAxBACDCABx"
    "xCCDxBDCDDxxDxCBAxACxBDxADABBCBBAxACADACBDDAxxCCAxCBDBBxxCBAADBCAAAxBDCBD"
    "ACACxBxDDDxBAxDDBDDDBBCxABxACDDxCAxCCxCADAABxBCBxxAxCACAADBDxABBDCDxCDxxB"
    "BBCCBDDABxCBABABABDCDAABDxBAAAxxDDCDxDCDAxDxDCxABCBABCxDxDBBCDCAAAAADCAAD"
    "DDxCDAADDBDxxDDBADACAxDxxDCxCCCxDDBAABABDBBDDABxxBBCCDCBCCBBBBBAxBABCCxxB"
    "DABDDxxADDBDBxBAABBxAxBDCAxxADACxCxDCADBDCDADxACDCDxCDDBABBxBCACDxCACAACx"
    "CABAAAABxBAAxACCxACADBCBBDADxDxDBxCCCDBBBAAAADxxBAxDxBDxxADDCCxCCCACxDxCD"
    "CCCCxDBCBCxBDxAABADCDBBxxDADCCxCBDxCxDBACCAABxDABDACCCxCDBxxACCDCBDCDBDBC"
    "xAACBxCAAxBADxBBxBBCCADxDCBBCDBxCCBCDAACDDBADxDBCADBxCDDxDCxBBADBxABxBABC"
    "BCCxADBxCBAABAxACBAxACDAACxDCBBxBDxxxDDDBBBDBxxACBDAACADBDDBCCCCxBxABAxBB"
    "DACDDxCDAxCADADCDDADACxxBADxxADABBAxxCCABBxxDAAxCDxBxxDBxCDBBABBCCADxCxAA"
    "DCCCCADBADxCCADCxACABCACxABBACBxAxxCBABBBACBBxABAxAxBABBBDAABAADxACxCADCD"
    "ABBxDCxDDDDxDDDDCABBBDCxACxBDABCCBBBxxCxCABxBADABACxAxDCBADADAABBADxABxCx"
    "CCCxCAxACBADDxCCCAxBBCxxBDBxACDxDDCxxCBDCxCxxCCDDCCxDCxCBBBBxBDCCAAxxDBAx"
    "BxBxADDCDCBxDDxAxABBAxDxCDDxCAxCDBACCxDBCxBCBAACxBAxBBDDAxCCBDxABBxBxxCCD"
    "xAxDDxCAACCxCBABCDCAA"
)


def get_one_value(enemy: str) -> int:
    if enemy in ['x', 'A']:
        return 0
    if enemy == 'B':
        return 1
    if enemy == 'C':
        return 3
    if enemy == 'D':
        return 5
    else:
        raise ValueError(
            f"Enemy must be A, B, C, D, or x! Got {enemy}"
        )

def get_n_values(enemies: str) -> int:
    if 'x' in enemies:
        real_enemies = ''.join([enemy for enemy in enemies if enemy != 'x'])
        return get_n_values(real_enemies)
    # `n` enemies custered together each get an (n-1) bonus
    # e.g. 2 enemies together each get +1, 3 together each get +2
    bonus = len(enemies) * (len(enemies) - 1)
    raw_value = sum([get_one_value(enemy) for enemy in enemies])
    if DEBUG_MODE:
        print(f'enemies: {enemies}, raw_value: {raw_value}, bonus: {bonus}')
    return raw_value + bonus

values = [
    get_n_values(input_str[i:i+CLUSTER_SIZE])
    for i in range(0, len(input_str), CLUSTER_SIZE)
]
if DEBUG_MODE:
    print(f'values: {values}')
total = sum(values)

print(f"Answer: {total}")