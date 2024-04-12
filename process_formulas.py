Loudness_mu=2.5049e-01
alphaRatio_mu=-2.6758e+00
hammarbergIndex_mu=9.1562e+00
slope0_500_mu=8.2642e-02
slope500_1500_mu=1.9943e-02
spectralFlux_mu=1.0016e-01
mfcc1_mu=2.1031e+01
mfcc2_mu=-2.0203e+01
mfcc3_mu=1.0336e+01
mfcc4_mu=-9.1172e+00
F0semitoneFrom27_5Hz_mu=8.1094e+00
jitterLocal_mu=4.5738e-03
shimmerLocaldB_mu= 2.9980e-01
HNRdBACF_mu=1.4062e+00
logRelF0_H1_H2_mu=2.5903e-01
logRelF0_H1_A3_mu=4.7461e+00
F1frequency_mu= 6.4250e+02
F1bandwidth_mu=9.8800e+02
F1amplitudeLogRelF0_mu=-1.4562e+02
F2frequency_mu=1.4210e+03
F2bandwidth_mu=8.6350e+02
F2amplitudeLogRelF0_mu=-1.4762e+02
F3frequency_mu=2.1780e+03
F3bandwidth_mu=7.6550e+02
F3amplitudeLogRelF0_mu=-1.4925e+02

Loudness_sigma=4.0520656e-01
alphaRatio_sigma=7.5566044e+00
hammarbergIndex_sigma=9.9376974e+00
slope0_500_sigma=2.6963402e-02
slope500_1500_sigma=3.4456372e-02
spectralFlux_sigma=2.2770199e-01
mfcc1_sigma=1.6510166e+01
mfcc2_sigma=1.5998608e+01
mfcc3_sigma=1.4597505e+01 
mfcc4_sigma=1.2892332e+01
F0semitoneFrom27_5Hz_sigma=1.3752241e+01
jitterLocal_sigma= 1.5122188e-02
shimmerLocaldB_sigma=6.4897507e-01
HNRdBACF_sigma= 2.9334540e+00 
logRelF0_H1_H2_sigma= 4.1907616e+00
logRelF0_H1_A3_sigma=9.6122217e+00 
F1frequency_sigma=3.5699408e+02
F1bandwidth_sigma=5.1291235e+02
F1amplitudeLogRelF0_sigma=8.8870285e+01
F2frequency_sigma=   7.0985553e+02
F2bandwidth_sigma=4.4298511e+02
F2amplitudeLogRelF0_sigma=8.5651329e+01
F3frequency_sigma=1.0818571e+03 
F3bandwidth_sigma= 3.8407300e+02 
F3amplitudeLogRelF0_sigma=8.3159859e+01

def get_vqf(llfs):
        Loudness_val=llfs[0]
        alphaRatio_val=llfs[1]
        hammarbergIndex_val=llfs[2]
        slope0_500_val=llfs[3]
        slope500_1500_val=llfs[4]
        spectralFlux_val=llfs[5]
        mfcc1_val=llfs[6]
        mfcc2_val=llfs[7]
        mfcc3_val=llfs[8]
        mfcc4_val=llfs[9]
        F0semitoneFrom27_5Hz_val=llfs[10]
        jitterLocal_val= llfs[11]
        shimmerLocaldB_val=llfs[12]
        HNRdBACF_val=llfs[13]
        logRelF0_H1_H2_val=llfs[14]
        logRelF0_H1_A3_val= llfs[15]
        F1frequency_val=llfs[16]
        F1bandwidth_val=llfs[17]
        F1amplitudeLogRelF0_val=llfs[18]
        F2frequency_val=llfs[19]
        F2bandwidth_val=llfs[20]
        F2amplitudeLogRelF0_val= llfs[21]
        F3frequency_val=llfs[22]
        F3bandwidth_val=llfs[23]
        F3amplitudeLogRelF0_val= llfs[24]
        # Compared the above indices with the orginal llf list adn they match so should be ok 
                
        Coveredness = 1/22 * ( + (0.75 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.75 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_mu  - spectralFlux_val) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.25 * (jitterLocal_mu  - jitterLocal_val) / jitterLocal_sigma )
        + (0.25 * (shimmerLocaldB_mu  - shimmerLocaldB_val) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_val - HNRdBACF_mu) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (1 * (F1frequency_val - F1frequency_mu) / F1frequency_sigma )
        + (0.25 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.25 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.25 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.25 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        )



        Aphonicity = 1/21 * ( + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_mu  - slope0_500_val) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_mu  - spectralFlux_val) / spectralFlux_sigma )
        + (0.75 * (mfcc1_mu  - mfcc1_val) / mfcc1_sigma )
        + (0.75 * (mfcc2_mu  - mfcc2_val) / mfcc2_sigma )
        + (0.75 * (mfcc3_mu  - mfcc3_val) / mfcc3_sigma )
        + (0.75 * (mfcc4_mu  - mfcc4_val) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_val - F1frequency_mu) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        )



        Biphonicity = 1/8 * ( + (0.25 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.25 * (slope0_500_mu  - slope0_500_val) / slope0_500_sigma )
        + (0.25 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_mu  - jitterLocal_val) / jitterLocal_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Breathiness = 1/21 * ( + (0.25 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (1 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_mu  - slope0_500_val) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (1 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.25 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (1 * (F1frequency_val - F1frequency_mu) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (1 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (1 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (1 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (1 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Creakiness = 1/25 * ( + (0.25 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.75 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_mu  - mfcc1_val) / mfcc1_sigma )
        + (0.75 * (mfcc2_mu  - mfcc2_val) / mfcc2_sigma )
        + (0.75 * (mfcc3_mu  - mfcc3_val) / mfcc3_sigma )
        + (0.75 * (mfcc4_mu  - mfcc4_val) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_val - logRelF0_H1_A3_mu) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_val - F2frequency_mu) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.25 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.25 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.25 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Diplophonicity = 1/21 * ( + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.25 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.25 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.25 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.25 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (0.25 * (logRelF0_H1_A3_val - logRelF0_H1_A3_mu) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.25 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (1 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.25 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (0.25 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Flutter = 1/8 * ( + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.25 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.25 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.25 * (HNRdBACF_val - HNRdBACF_mu) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.25 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        )



        Glottalization = 1/22 * ( + (0.75 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_val - hammarbergIndex_mu) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_mu  - mfcc1_val) / mfcc1_sigma )
        + (0.75 * (mfcc2_mu  - mfcc2_val) / mfcc2_sigma )
        + (0.75 * (mfcc3_mu  - mfcc3_val) / mfcc3_sigma )
        + (0.75 * (mfcc4_mu  - mfcc4_val) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.25 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (0.25 * (F1frequency_val - F1frequency_mu) / F1frequency_sigma )
        + (0.25 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.25 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Hoarseness = 1/20 * ( + (0.75 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (1 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.25 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.25 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (1 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Roughness = 1/23 * ( + (0.25 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (0.25 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.25 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_mu  - mfcc1_val) / mfcc1_sigma )
        + (0.75 * (mfcc2_mu  - mfcc2_val) / mfcc2_sigma )
        + (0.75 * (mfcc3_mu  - mfcc3_val) / mfcc3_sigma )
        + (0.75 * (mfcc4_mu  - mfcc4_val) / mfcc4_sigma )
        + (0.25 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (1 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.25 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.25 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.25 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.25 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.25 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.25 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.25 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.25 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.25 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Nasality = 1/21 * ( + (0.75 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_val - hammarbergIndex_mu) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (1 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Jitter = 1/11 * ( + (0.25 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.25 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (1 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.25 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.25 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        )



        Pressed = 1/14 * ( + (0.25 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_val - logRelF0_H1_A3_mu) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_val - F1frequency_mu) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_val - F2frequency_mu) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Pulsed = 1/13 * ( + (0.75 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (1 * (hammarbergIndex_val - hammarbergIndex_mu) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (0.25 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.25 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.25 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.25 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.25 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        )



        Resonant = 1/19 * ( + (0.25 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (slope0_500_mu  - slope0_500_val) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (1 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (1 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (1 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (1 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (HNRdBACF_val - HNRdBACF_mu) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_val - logRelF0_H1_A3_mu) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (1 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (1 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (1 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (1 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Shimmer = 1/15 * ( + (0.25 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.25 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (1 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.25 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.25 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.25 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.25 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.25 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.25 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.25 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.25 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (0.25 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Strained = 1/19 * ( + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (1 * (hammarbergIndex_val - hammarbergIndex_mu) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.25 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.25 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Strohbassness = 1/21 * ( + (1 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.25 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (1 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_mu  - mfcc2_val) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_mu  - mfcc4_val) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.25 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.25 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (1 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (1 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Tremor = 1/20 * ( + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_val - hammarbergIndex_mu) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_mu  - slope0_500_val) / slope0_500_sigma )
        + (0.75 * (slope500_1500_mu  - slope500_1500_val) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_val - jitterLocal_mu) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (1 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        )



        Twanginess = 1/22 * ( + (0.25 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (alphaRatio_val - alphaRatio_mu) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_val - hammarbergIndex_mu) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.25 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (1 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.25 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_mu  - jitterLocal_val) / jitterLocal_sigma )
        + (0.25 * (shimmerLocaldB_val - shimmerLocaldB_mu) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_val - HNRdBACF_mu) / HNRdBACF_sigma )
        + (1 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (1 * (logRelF0_H1_A3_val - logRelF0_H1_A3_mu) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.25 * (F2frequency_val - F2frequency_mu) / F2frequency_sigma )
        + (1 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Ventricular = 1/23 * ( + (0.25 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        + (0.75 * (alphaRatio_mu  - alphaRatio_val) / alphaRatio_sigma )
        + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_mu  - slope0_500_val) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_mu  - F0semitoneFrom27_5Hz_val) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_mu  - jitterLocal_val) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_mu  - shimmerLocaldB_val) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_mu  - HNRdBACF_val) / HNRdBACF_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_val - F1amplitudeLogRelF0_mu) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_mu  - F2frequency_val) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_mu  - F2bandwidth_val) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_mu  - F3bandwidth_val) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_val - F3amplitudeLogRelF0_mu) / F3amplitudeLogRelF0_sigma )
        )



        Wobble = 1/15 * ( + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (logRelF0_H1_H2_mu  - logRelF0_H1_H2_val) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_mu  - logRelF0_H1_A3_val) / logRelF0_H1_A3_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_mu  - F1bandwidth_val) / F1bandwidth_sigma )
        + (0.25 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2amplitudeLogRelF0_mu  - F2amplitudeLogRelF0_val) / F2amplitudeLogRelF0_sigma )
        + (0.25 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.25 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        + (0.75 * (F3amplitudeLogRelF0_mu  - F3amplitudeLogRelF0_val) / F3amplitudeLogRelF0_sigma )
        )



        Yawniness = 1/21 * ( + (0.75 * (hammarbergIndex_mu  - hammarbergIndex_val) / hammarbergIndex_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (jitterLocal_mu  - jitterLocal_val) / jitterLocal_sigma )
        + (0.75 * (shimmerLocaldB_mu  - shimmerLocaldB_val) / shimmerLocaldB_sigma )
        + (0.75 * (HNRdBACF_val - HNRdBACF_mu) / HNRdBACF_sigma )
        + (0.75 * (logRelF0_H1_H2_val - logRelF0_H1_H2_mu) / logRelF0_H1_H2_sigma )
        + (0.75 * (logRelF0_H1_A3_val - logRelF0_H1_A3_mu) / logRelF0_H1_A3_sigma )
        + (1 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.75 * (F1amplitudeLogRelF0_mu  - F1amplitudeLogRelF0_val) / F1amplitudeLogRelF0_sigma )
        + (0.75 * (F2frequency_val - F2frequency_mu) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_mu  - F3frequency_val) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        )



        Loudness = 1/17 * ( + (1 * (Loudness_val - Loudness_mu) / Loudness_sigma )
        + (0.75 * (slope0_500_val - slope0_500_mu) / slope0_500_sigma )
        + (0.75 * (slope500_1500_val - slope500_1500_mu) / slope500_1500_sigma )
        + (0.75 * (spectralFlux_val - spectralFlux_mu) / spectralFlux_sigma )
        + (0.75 * (mfcc1_val - mfcc1_mu) / mfcc1_sigma )
        + (0.75 * (mfcc2_val - mfcc2_mu) / mfcc2_sigma )
        + (0.75 * (mfcc3_val - mfcc3_mu) / mfcc3_sigma )
        + (0.75 * (mfcc4_val - mfcc4_mu) / mfcc4_sigma )
        + (0.75 * (F0semitoneFrom27_5Hz_val - F0semitoneFrom27_5Hz_mu) / F0semitoneFrom27_5Hz_sigma )
        + (0.75 * (HNRdBACF_val - HNRdBACF_mu) / HNRdBACF_sigma )
        + (0.75 * (F1frequency_mu  - F1frequency_val) / F1frequency_sigma )
        + (0.75 * (F1bandwidth_val - F1bandwidth_mu) / F1bandwidth_sigma )
        + (0.75 * (F2frequency_val - F2frequency_mu) / F2frequency_sigma )
        + (0.75 * (F2bandwidth_val - F2bandwidth_mu) / F2bandwidth_sigma )
        + (0.75 * (F2amplitudeLogRelF0_val - F2amplitudeLogRelF0_mu) / F2amplitudeLogRelF0_sigma )
        + (0.75 * (F3frequency_val - F3frequency_mu) / F3frequency_sigma )
        + (0.75 * (F3bandwidth_val - F3bandwidth_mu) / F3bandwidth_sigma )
        )

        res = { }
        vals =  [Coveredness, Aphonicity, Biphonicity, Breathiness,Creakiness,Diplophonicity,Flutter,Glottalization,Hoarseness,Roughness,\
                Nasality,Jitter,Pressed,Pulsed,Resonant,Shimmer,Strained,Strohbassness,Tremor,Twanginess,Ventricular,Wobble,Yawniness,Loudness]
        columns = ['Coveredness' ,'Aphonicity' ,'Biphonicity','Breathiness','Creakiness','Diplophonicity','Flutter','Glottalization','Hoarseness','Roughness',\
                'Nasality','Jitter','Pressed','Pulsed','Resonant','Shimmer','Strained','Strohbassness','Tremor','Twanginess','Ventricular','Wobble','Yawniness','Loudness']
        
        for c,v in zip(columns, vals):
                res[c] = v
            
        return res

Coveredness_mu=-0.00437442449                                                                                                                                                                                   
Aphonicity_mu=0.00365292386
Biphonicity_mu=0.00461800099
Breathiness_mu=0.00824773966                                                                                                                                                                                     
Creakiness_mu=0.00259605654
Diplophonicity_mu=-0.00408232511
Flutter_mu=0.00689502579
Glottalization_mu=0.00964083852
Hoarseness_mu=-0.00124529919
Roughness_mu=0.00203502914
Nasality_mu=-0.019710842
Jitter_mu=0.00265922633
Pressed_mu=-0.00383037557
Pulsed_mu=0.0015846288
Resonant_mu=-0.0276369177
Shimmer_mu=-0.00736826286
Strained_mu=-0.0098922629
Strohbassness_mu=-0.00275738596
Tremor_mu=0.00403362926
Twanginess_mu=-0.0106778728
Ventricular_mu=-0.0192278368
Wobble_mu=-0.00947008148
Yawniness_mu=3.37747586e-05
Loudness_mu=0.00673008907


Coveredness_sigma=0.02904816                                                                                                                                                                                     
Aphonicity_sigma=0.05168905                                                                                                                                                                                      
Biphonicity_sigma=0.06223224
Breathiness_sigma=0.05059166
Creakiness_sigma=0.03797493
Diplophonicity_sigma=0.02079254
Flutter_sigma=0.06842278
Glottalization_sigma=0.05716338
Hoarseness_sigma=0.03520896
Roughness_sigma=0.02897984
Nasality_sigma=0.0725326
Jitter_sigma=0.04478104
Pressed_sigma=0.05601011
Pulsed_sigma=0.06059067
Resonant_sigma=0.101135
Shimmer_sigma=0.03847137
Strained_sigma=0.06445844
Strohbassness_sigma=0.04592833
Tremor_sigma=0.05712063
Twanginess_sigma=0.0632771
Ventricular_sigma=0.07818535
Wobble_sigma=0.04451978
Yawniness_sigma=0.03724454
Loudness_sigma=0.07929499

def get_ocean(vqfs):

        Coveredness_val=vqfs[0]                                                                                                                                                                                          
        Aphonicity_val=vqfs[1]                                                                                                                                                                                           
        Biphonicity_val=vqfs[2]
        Breathiness_val=vqfs[3]
        Creakiness_val=vqfs[4]
        Diplophonicity_val=vqfs[5]
        Flutter_val=vqfs[6]
        Glottalization_val=vqfs[7]
        Hoarseness_val=vqfs[8]
        Roughness_val=vqfs[9]
        Nasality_val=vqfs[10]
        Jitter_val=vqfs[11]
        Pressed_val=vqfs[12]
        Pulsed_val=vqfs[13]
        Resonant_val=vqfs[14]
        Shimmer_val=vqfs[15]
        Strained_val=vqfs[16]
        Strohbassness_val=vqfs[17]
        Tremor_val=vqfs[18]
        Twanginess_val=vqfs[19]
        Ventricular_val=vqfs[20]
        Wobble_val=vqfs[21]
        Yawniness_val=vqfs[22]
        Loudness_val=vqfs[23]

        Openness = 1/15 * ( + (0.75 * (Coveredness_mu  - Coveredness_val) / Coveredness_sigma )
                + (0.75 * (Aphonicity_mu  - Aphonicity_val) / Aphonicity_sigma )
                + (0.75 * (Biphonicity_val - Biphonicity_mu) / Biphonicity_sigma )
                + (0.25 * (Breathiness_val - Breathiness_mu) / Breathiness_sigma )
                + (0.25 * (Hoarseness_mu  - Hoarseness_val) / Hoarseness_sigma )
                + (0.25 * (Roughness_mu  - Roughness_val) / Roughness_sigma )
                + (0.75 * (Nasality_mu  - Nasality_val) / Nasality_sigma )
                + (0.75 * (Jitter_mu  - Jitter_val) / Jitter_sigma )
                + (0.75 * (Pressed_val - Pressed_mu) / Pressed_sigma )
                + (0.75 * (Pulsed_mu  - Pulsed_val) / Pulsed_sigma )
                + (0.75 * (Resonant_val - Resonant_mu) / Resonant_sigma )
                + (0.25 * (Strained_mu  - Strained_val) / Strained_sigma )
                + (0.25 * (Twanginess_val - Twanginess_mu) / Twanginess_sigma )
                + (0.25 * (Yawniness_mu  - Yawniness_val) / Yawniness_sigma )
                + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
                )



        Conscientiousness = 1/17 * ( + (0.75 * (Aphonicity_mu  - Aphonicity_val) / Aphonicity_sigma )
                + (0.25 * (Biphonicity_val - Biphonicity_mu) / Biphonicity_sigma )
                + (0.25 * (Breathiness_mu  - Breathiness_val) / Breathiness_sigma )
                + (0.25 * (Hoarseness_mu  - Hoarseness_val) / Hoarseness_sigma )
                + (0.25 * (Roughness_mu  - Roughness_val) / Roughness_sigma )
                + (0.75 * (Nasality_mu  - Nasality_val) / Nasality_sigma )
                + (0.75 * (Jitter_mu  - Jitter_val) / Jitter_sigma )
                + (0.75 * (Pressed_val - Pressed_mu) / Pressed_sigma )
                + (0.75 * (Pulsed_mu  - Pulsed_val) / Pulsed_sigma )
                + (0.75 * (Resonant_val - Resonant_mu) / Resonant_sigma )
                + (0.25 * (Shimmer_mu  - Shimmer_val) / Shimmer_sigma )
                + (0.25 * (Strained_mu  - Strained_val) / Strained_sigma )
                + (0.25 * (Tremor_mu  - Tremor_val) / Tremor_sigma )
                + (0.75 * (Twanginess_val - Twanginess_mu) / Twanginess_sigma )
                + (0.25 * (Wobble_mu  - Wobble_val) / Wobble_sigma )
                + (0.25 * (Yawniness_mu  - Yawniness_val) / Yawniness_sigma )
                + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
                )

        Extraversion = 1/14 * ( + (0.75 * (Coveredness_mu  - Coveredness_val) / Coveredness_sigma )
                               + (0.75 * (Aphonicity_mu  - Aphonicity_val) / Aphonicity_sigma )
                               + (0.25 * (Breathiness_val - Breathiness_mu) / Breathiness_sigma )
                               + (0.25 * (Hoarseness_mu  - Hoarseness_val) / Hoarseness_sigma )
                               + (0.25 * (Roughness_mu  - Roughness_val) / Roughness_sigma )
                               + (0.75 * (Nasality_mu  - Nasality_val) / Nasality_sigma )
                               + (0.75 * (Jitter_mu  - Jitter_val) / Jitter_sigma )
                               + (0.75 * (Pressed_val - Pressed_mu) / Pressed_sigma )
                               + (0.75 * (Pulsed_mu  - Pulsed_val) / Pulsed_sigma ) 
                               + (0.75 * (Resonant_val - Resonant_mu) / Resonant_sigma )
                                + (0.25 * (Strained_mu  - Strained_val) / Strained_sigma )
                                + (0.25 * (Twanginess_val - Twanginess_mu) / Twanginess_sigma )
                                + (0.25 * (Yawniness_mu  - Yawniness_val) / Yawniness_sigma )
                                + (0.75 * (Loudness_val - Loudness_mu) / Loudness_sigma )
                                                                ) 

        Agreeableness = 1/14 * ( + (0.75 * (Coveredness_val - Coveredness_mu) / Coveredness_sigma )
                                + (0.75 * (Aphonicity_mu  - Aphonicity_val) / Aphonicity_sigma ) 
                                + (0.25 * (Breathiness_val - Breathiness_mu) / Breathiness_sigma )
                                + (0.25 * (Hoarseness_mu  - Hoarseness_val) / Hoarseness_sigma ) 
                                + (0.25 * (Roughness_mu  - Roughness_val) / Roughness_sigma ) 
                                + (0.75 * (Nasality_mu  - Nasality_val) / Nasality_sigma )
                                + (0.75 * (Jitter_mu  - Jitter_val) / Jitter_sigma ) 
                                + (0.75 * (Pressed_mu  - Pressed_val) / Pressed_sigma )
                                + (0.75 * (Pulsed_mu  - Pulsed_val) / Pulsed_sigma )
                                + (0.75 * (Resonant_val - Resonant_mu) / Resonant_sigma )
                                + (0.25 * (Strained_mu  - Strained_val) / Strained_sigma )
                                + (0.25 * (Twanginess_val - Twanginess_mu) / Twanginess_sigma )
                                + (0.25 * (Yawniness_val - Yawniness_mu) / Yawniness_sigma ) 
                                + (0.25 * (Loudness_mu  - Loudness_val) / Loudness_sigma ))
        

        Neuroticism = 1/18 * ( + (0.75 * (Coveredness_val - Coveredness_mu) / Coveredness_sigma )
        + (0.75 * (Aphonicity_val - Aphonicity_mu) / Aphonicity_sigma )
        + (0.75 * (Breathiness_val - Breathiness_mu) / Breathiness_sigma )
        + (0.75 * (Flutter_val - Flutter_mu) / Flutter_sigma )
        + (0.75 * (Hoarseness_val - Hoarseness_mu) / Hoarseness_sigma )
        + (0.75 * (Roughness_val - Roughness_mu) / Roughness_sigma )
        + (0.75 * (Nasality_val - Nasality_mu) / Nasality_sigma )
        + (0.75 * (Jitter_val - Jitter_mu) / Jitter_sigma )
        + (0.75 * (Pressed_mu  - Pressed_val) / Pressed_sigma )
        + (0.75 * (Pulsed_val - Pulsed_mu) / Pulsed_sigma )
        + (0.75 * (Resonant_mu  - Resonant_val) / Resonant_sigma )
        + (0.75 * (Shimmer_val - Shimmer_mu) / Shimmer_sigma )
        + (0.75 * (Strained_val - Strained_mu) / Strained_sigma )
        + (0.75 * (Tremor_val - Tremor_mu) / Tremor_sigma )
        + (0.75 * (Twanginess_mu  - Twanginess_val) / Twanginess_sigma )
        + (0.75 * (Wobble_val - Wobble_mu) / Wobble_sigma )
        + (0.75 * (Yawniness_val - Yawniness_mu) / Yawniness_sigma )
        + (0.75 * (Loudness_mu  - Loudness_val) / Loudness_sigma )
        )  

        res = { }
        vals = [Openness,Conscientiousness,Extraversion,Agreeableness,Neuroticism]
        columns = ['Openness','Conscientiousness','Extraversion','Agreeableness','Neuroticism']
        for c,v in zip(columns, vals):
                res[c] = v
            
        return res
# import matplotlib.pyplot as plt 

# rows = [ 'Loudness', 'alphaRatio','hammarbergIndex','slope0_500','slope500_1500','spectralFlux','mfcc1','mfcc2','mfcc3','mfcc4',\
#         'F0semitoneFrom27_5Hz','jitterLocal','shimmerLocaldB','HNRdBACF','logRelF0_H1_H2','logRelF0_H1_A3','F1frequency','F1bandwidth',\
#         'F1amplitudeLogRelF0','F2frequency','F2bandwidth' ,'F2amplitudeLogRelF0','F3frequency' ,'F3bandwidth','F3amplitudeLogRelF0'] # llf       
# columns=['Coveredness' ,'Aphonicity' ,'Biphonicity','Breathiness','Creakiness','Diplophonicity','Flutter','Glottalization','Hoarseness','Roughness',\
#         'Nasality','Jitter','Pressed','Pulsed','Resonant','Shimmer','Strained','Strohbassness','Tremor','Twanginess','Ventricular','Wobble','Yawniness','Loudness']

# yaxis = [Coveredness ,Aphonicity ,Biphonicity,Breathiness,Creakiness,Diplophonicity,Flutter,Glottalization,Hoarseness,Roughness,\
#         Nasality,Jitter,Pressed,Pulsed,Resonant,Shimmer,Strained,Strohbassness,Tremor,Twanginess,Ventricular,Wobble,Yawniness,Loudness]

# plt.figure(figsize=(20,5))
# plt.plot(columns, yaxis, 's')
# plt.xticks(rotation=90)
# plt.savefig('formula_plot.png')
