/*******************************************************************************
* File Name: PushB.h  
* Version 2.20
*
* Description:
*  This file contains Pin function prototypes and register defines
*
* Note:
*
********************************************************************************
* Copyright 2008-2015, Cypress Semiconductor Corporation.  All rights reserved.
* You may use this file only in accordance with the license, terms, conditions, 
* disclaimers, and limitations in the end user license agreement accompanying 
* the software package with which this file was provided.
*******************************************************************************/

#if !defined(CY_PINS_PushB_H) /* Pins PushB_H */
#define CY_PINS_PushB_H

#include "cytypes.h"
#include "cyfitter.h"
#include "cypins.h"
#include "PushB_aliases.h"

/* APIs are not generated for P15[7:6] */
#if !(CY_PSOC5A &&\
	 PushB__PORT == 15 && ((PushB__MASK & 0xC0) != 0))


/***************************************
*        Function Prototypes             
***************************************/    

/**
* \addtogroup group_general
* @{
*/
void    PushB_Write(uint8 value);
void    PushB_SetDriveMode(uint8 mode);
uint8   PushB_ReadDataReg(void);
uint8   PushB_Read(void);
void    PushB_SetInterruptMode(uint16 position, uint16 mode);
uint8   PushB_ClearInterrupt(void);
/** @} general */

/***************************************
*           API Constants        
***************************************/
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup driveMode Drive mode constants
     * \brief Constants to be passed as "mode" parameter in the PushB_SetDriveMode() function.
     *  @{
     */
        #define PushB_DM_ALG_HIZ         PIN_DM_ALG_HIZ
        #define PushB_DM_DIG_HIZ         PIN_DM_DIG_HIZ
        #define PushB_DM_RES_UP          PIN_DM_RES_UP
        #define PushB_DM_RES_DWN         PIN_DM_RES_DWN
        #define PushB_DM_OD_LO           PIN_DM_OD_LO
        #define PushB_DM_OD_HI           PIN_DM_OD_HI
        #define PushB_DM_STRONG          PIN_DM_STRONG
        #define PushB_DM_RES_UPDWN       PIN_DM_RES_UPDWN
    /** @} driveMode */
/** @} group_constants */
    
/* Digital Port Constants */
#define PushB_MASK               PushB__MASK
#define PushB_SHIFT              PushB__SHIFT
#define PushB_WIDTH              1u

/* Interrupt constants */
#if defined(PushB__INTSTAT)
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup intrMode Interrupt constants
     * \brief Constants to be passed as "mode" parameter in PushB_SetInterruptMode() function.
     *  @{
     */
        #define PushB_INTR_NONE      (uint16)(0x0000u)
        #define PushB_INTR_RISING    (uint16)(0x0001u)
        #define PushB_INTR_FALLING   (uint16)(0x0002u)
        #define PushB_INTR_BOTH      (uint16)(0x0003u) 
    /** @} intrMode */
/** @} group_constants */

    #define PushB_INTR_MASK      (0x01u) 
#endif /* (PushB__INTSTAT) */


/***************************************
*             Registers        
***************************************/

/* Main Port Registers */
/* Pin State */
#define PushB_PS                     (* (reg8 *) PushB__PS)
/* Data Register */
#define PushB_DR                     (* (reg8 *) PushB__DR)
/* Port Number */
#define PushB_PRT_NUM                (* (reg8 *) PushB__PRT) 
/* Connect to Analog Globals */                                                  
#define PushB_AG                     (* (reg8 *) PushB__AG)                       
/* Analog MUX bux enable */
#define PushB_AMUX                   (* (reg8 *) PushB__AMUX) 
/* Bidirectional Enable */                                                        
#define PushB_BIE                    (* (reg8 *) PushB__BIE)
/* Bit-mask for Aliased Register Access */
#define PushB_BIT_MASK               (* (reg8 *) PushB__BIT_MASK)
/* Bypass Enable */
#define PushB_BYP                    (* (reg8 *) PushB__BYP)
/* Port wide control signals */                                                   
#define PushB_CTL                    (* (reg8 *) PushB__CTL)
/* Drive Modes */
#define PushB_DM0                    (* (reg8 *) PushB__DM0) 
#define PushB_DM1                    (* (reg8 *) PushB__DM1)
#define PushB_DM2                    (* (reg8 *) PushB__DM2) 
/* Input Buffer Disable Override */
#define PushB_INP_DIS                (* (reg8 *) PushB__INP_DIS)
/* LCD Common or Segment Drive */
#define PushB_LCD_COM_SEG            (* (reg8 *) PushB__LCD_COM_SEG)
/* Enable Segment LCD */
#define PushB_LCD_EN                 (* (reg8 *) PushB__LCD_EN)
/* Slew Rate Control */
#define PushB_SLW                    (* (reg8 *) PushB__SLW)

/* DSI Port Registers */
/* Global DSI Select Register */
#define PushB_PRTDSI__CAPS_SEL       (* (reg8 *) PushB__PRTDSI__CAPS_SEL) 
/* Double Sync Enable */
#define PushB_PRTDSI__DBL_SYNC_IN    (* (reg8 *) PushB__PRTDSI__DBL_SYNC_IN) 
/* Output Enable Select Drive Strength */
#define PushB_PRTDSI__OE_SEL0        (* (reg8 *) PushB__PRTDSI__OE_SEL0) 
#define PushB_PRTDSI__OE_SEL1        (* (reg8 *) PushB__PRTDSI__OE_SEL1) 
/* Port Pin Output Select Registers */
#define PushB_PRTDSI__OUT_SEL0       (* (reg8 *) PushB__PRTDSI__OUT_SEL0) 
#define PushB_PRTDSI__OUT_SEL1       (* (reg8 *) PushB__PRTDSI__OUT_SEL1) 
/* Sync Output Enable Registers */
#define PushB_PRTDSI__SYNC_OUT       (* (reg8 *) PushB__PRTDSI__SYNC_OUT) 

/* SIO registers */
#if defined(PushB__SIO_CFG)
    #define PushB_SIO_HYST_EN        (* (reg8 *) PushB__SIO_HYST_EN)
    #define PushB_SIO_REG_HIFREQ     (* (reg8 *) PushB__SIO_REG_HIFREQ)
    #define PushB_SIO_CFG            (* (reg8 *) PushB__SIO_CFG)
    #define PushB_SIO_DIFF           (* (reg8 *) PushB__SIO_DIFF)
#endif /* (PushB__SIO_CFG) */

/* Interrupt Registers */
#if defined(PushB__INTSTAT)
    #define PushB_INTSTAT            (* (reg8 *) PushB__INTSTAT)
    #define PushB_SNAP               (* (reg8 *) PushB__SNAP)
    
	#define PushB_0_INTTYPE_REG 		(* (reg8 *) PushB__0__INTTYPE)
#endif /* (PushB__INTSTAT) */

#endif /* CY_PSOC5A... */

#endif /*  CY_PINS_PushB_H */


/* [] END OF FILE */
